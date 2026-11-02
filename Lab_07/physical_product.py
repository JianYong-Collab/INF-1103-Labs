from product import Product
from interfaces import CanBeShipped
from constants import COST_PER_KILOGRAM
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
