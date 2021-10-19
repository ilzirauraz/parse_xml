import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element

from db.DB import DB

from models.models import PurchaseOrder, Address, Item


xml_file = 'test_xml.xml'

db = DB()
db.run_migrations()


def parse_file(path: str):
    """Основной метод парсинга файла."""
    tree = ET.parse(path)
    root = tree.getroot()

    for order_node in root:
        purchase_order_number = order_node.attrib.get('PurchaseOrderNumber')

        parse_order(order_node, purchase_order_number)

        for node in order_node:
            if node.tag == "Address":
                parse_address(node, purchase_order_number)

            if node.tag == "Items":
                for item_node in node:
                    parse_item(item_node, purchase_order_number)


def parse_order(order_node: Element, purchase_order_number: int):
    """Сбор и сохранение данных по заказам."""
    purchase_order_data = {}
    purchase_order_data['PurchaseOrderNumber'] = purchase_order_number
    purchase_order_data['OrderDate'] = order_node.attrib.get('OrderDate')
    purchase_order_data['DeliveryNotes'] = order_node.find('DeliveryNotes').text

    # Валидация данных
    purchase_order = PurchaseOrder.parse_obj(purchase_order_data)
    db.save("PurchaseOrders", purchase_order)


def parse_address(node: Element, purchase_order_number: int):
    """Сбор и сохранение данных по адресам."""
    address_data = {}
    address_data['PurchaseOrderNumber'] = purchase_order_number
    address_data["Type"] = node.attrib.get('Type')

    for address_attrs in node:
        address_data[address_attrs.tag] = address_attrs.text

    # Валидация данных
    address = Address.parse_obj(address_data)
    db.save('Addresses', address)


def parse_item(node: Element, purchase_order_number: int):
    """Сбор и сохранение данных по товарам."""
    item_data = {}
    item_data['PurchaseOrderNumber'] = purchase_order_number
    item_data['PartNumber'] = node.attrib.get('PartNumber')
    for item_attr in node:
        item_data[item_attr.tag] = item_attr.text

    # Валидация данных
    item = Item.parse_obj(item_data)
    db.save('Items', item)


if __name__ == '__main__':
    parse_file(xml_file)
