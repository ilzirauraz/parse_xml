from sqlite3 import Connection, Error

CREATE_PURCHASE_ORDER_QUERY = '''CREATE TABLE IF NOT EXISTS PurchaseOrders
                                    (
                                        PurchaseOrderNumber INTEGER NOT NULL UNIQUE PRIMARY KEY ,
                                        OrderDate           DATETIME NOT NULL,
                                        DeliveryNotes       TEXT
                                    ); '''

CREATE_ADDRESS_QUERY_QUERY = '''CREATE TABLE IF NOT EXISTS Addresses
                                    (
                                        id                  INTEGER PRIMARY KEY,
                                        PurchaseOrderNumber INTEGER NOT NULL,
                                        Type                TEXT,
                                        Name                TEXT,
                                        Street              TEXT,
                                        City                TEXT,
                                        State               TEXT,
                                        Zip                 INTEGER,
                                        Country             TEXT,
                                        FOREIGN KEY (PurchaseOrderNumber) REFERENCES PurchaseOrder (
                                        PurchaseOrderNumber)
                                    ); '''

CREATR_ITEMS_QUERY = '''CREATE TABLE IF NOT EXISTS Items
                            (
                                id                  INTEGER PRIMARY KEY,
                                PurchaseOrderNumber INTEGER NOT NULL,
                                PartNumber          TEXT,
                                ProductName         TEXT,
                                Quantity            INTEGER,
                                USPrice             TEXT,
                                Comment             TEXT,
                                ShipDate            TEXT,
                                FOREIGN KEY (PurchaseOrderNumber) REFERENCES PurchaseOrder (
                                PurchaseOrderNumber)
                            ); '''


def run(conn: Connection):
    try:
        cursor = conn.cursor()
        cursor.execute(CREATE_PURCHASE_ORDER_QUERY)
        cursor.execute(CREATE_ADDRESS_QUERY_QUERY)
        cursor.execute(CREATR_ITEMS_QUERY)
        conn.commit()
        print("Таблицы созданы")
        cursor.close()
        conn.close()

    except Error as error:
        print("Ошибка при подключении к sqlite", error)
