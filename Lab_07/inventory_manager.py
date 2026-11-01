import copy
from interfaces import CanBeShipped
from abc import ABC, abstractmethod
from constants import COST_PER_KILOGRAM
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

class PhysicalProduct(Product, CanBeShipped):
    __weight : float

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f" | Weight: {self.__weight}")

    def get_fulfilment_info(self):
        print("This product requires physical shipping")

    def calculate_shipping_cost(self):
        print(f"The shipping cost is {self.__weight * COST_PER_KILOGRAM}")
    
    def to_dict(self):
        dict = super().to_dict()
        dict.update({"weight" : self.__weight})
        return dict

class DigitalProduct(Product):
    __download_size : int

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f" | Download Size: {self.__download_size}")

    def get_fulfilment_info(self):
        print("This product is delivered digitally")

    def to_dict(self):
        dict = super().to_dict()
        dict.update({"download_size" : self.__download_size})
        return dict

class Inventory():
    __product_list : list[Product]

    # Sets Inventory to empty list unless specified
    def __init__(self, current_productlist = None):

        if current_productlist is None:
            self.__product_list = []
        else:
            self.__product_list = copy.deepcopy(current_productlist)

    def add_product(self, target_product: Product):
        # Update Stock
        for product in self.__product_list:
            if target_product.id == product.id:
                return False

        self.__product_list.append(target_product)
        # Sorting
        self.__product_list.sort(key=lambda p : p.id)

        return True

    def search_product(self, product_id: str):
        for product in self.__product_list:
            if(product.id == product_id):
                return product

    def update_inventory_stock(self, product_id : str, new_stock : int):
        for product in self.__product_list:
            if product.id == product_id:
                product.update_stock(new_stock)

    def display_all(self):
        for product in self.__product_list:
            product.display_information()

    @property
    def inventory(self):
        return self.__product_list

    def set_inventory(self, current_productlist):
        self.__product_list = copy.deepcopy(current_productlist)