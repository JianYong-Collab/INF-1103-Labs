from abc import ABC, abstractmethod
from supplier import Supplier
class Product(ABC):
    # Protected Variables
    _product_id : str
    _name : str
    _price : float
    _stock : int
    _supplier: Supplier
    
    # Methods
    def __init__(self, product_id : str, name : str , price : float , stock : int
                 ,  supplier: Supplier = None) -> None:
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock
        self._supplier = supplier

    def update_stock(self, quantity: int) -> None:
        self._stock = quantity

    def display_information(self) -> None:
        self._supplier.display_information()
        print(f"ID: {self._product_id} | Name: {self._name} | Price: {self._price:.2f} | Stock: {self._stock}",end="")

    @property
    def id(self) -> str:
        return self._product_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def stock(self) -> int:
        return self._stock

    @property
    def supplier(self) -> Supplier:
        return self._supplier
        
    
    def to_dict(self) -> dict:
        return{
            "product_type" : self.__class__.__name__,
            "supplier_id": self._supplier.supplier_id,
            "supplier_name": self._supplier.name,
            "supplier_email": self._supplier.contact_email,
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock,
        }

    @abstractmethod
    def get_fulfilment_info(self):
        pass
