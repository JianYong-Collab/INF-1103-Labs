import copy
from product import Product

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