import copy
class Product():
    # Variables
    __product_id : str
    __name : str
    __price : float
    __stock : int

    # Methods
    def __init__(self, product_id : str, name : str , price : float , stock : int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity: int):
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: {self.__price:.2f} | Stock: {self.__stock}")

    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def to_dict(self):
        return{
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

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
            if target_product.get_id() == product.get_id():
                return False

        self.__product_list.append(target_product)
        # Sorting
        self.__product_list.sort(key=lambda p : p.get_id())

        return True

    def search_product(self, product_id: str):
        for product in self.__product_list:
            if(product.get_id() == product_id):
                return product

    def update_inventory_stock(self, product_id : str, new_stock : int):
        for product in self.__product_list:
            if product.get_id() == product_id:
                product.update_stock(new_stock)

    def display_all(self):
        for product in self.__product_list:
            product.display_information()

    def get_inventory(self):
        return self.__product_list

    def set_inventory(self, current_productlist):
        self.__product_list = copy.deepcopy(current_productlist)