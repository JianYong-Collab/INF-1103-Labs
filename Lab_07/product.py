from abc import ABC, abstractmethod
class Product(ABC):
    # Protected Variables
    _product_id : str
    _name : str
    _price : float
    _stock : int
    
    # Methods
    def __init__(self, product_id : str, name : str , price : float , stock : int):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    def update_stock(self, quantity: int):
        self._stock = quantity

    def display_information(self):
        print(f"ID: {self._product_id} | Name: {self._name} | Price: {self._price:.2f} | Stock: {self._stock}",end="")

    @property
    def id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock
        
    
    def to_dict(self):
        return{
            "product_type" : self.__class__.__name__,
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock
        }

    @abstractmethod
    def get_fulfilment_info(self):
        pass
