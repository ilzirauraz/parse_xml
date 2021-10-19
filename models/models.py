from pydantic import BaseModel
from typing import Optional


class PurchaseOrder(BaseModel):
    PurchaseOrderNumber: int
    OrderDate: str
    DeliveryNotes: str


class Address(BaseModel):
    PurchaseOrderNumber: int
    Type: str
    Name: str
    Street: str
    City: str
    State: str
    Zip: int
    Country: str


class Item(BaseModel):
    PurchaseOrderNumber: int
    PartNumber: str
    ProductName: str
    Quantity: int
    USPrice: str
    Comment: Optional[str] = ''
    ShipDate: Optional[str] = ''
