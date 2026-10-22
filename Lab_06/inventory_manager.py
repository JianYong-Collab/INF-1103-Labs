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


class Inventory():
    __product_list : list[Product]


    # Sets Inventory to empty list unless specified
    def __init__(self, current_productlist = []):
        self.__product_list = current_productlist

    def add_product(self, product: Product):
        self.__product_list.append(product)

    def search_product(self, product_id: str):
        for product in self.__product_list:
            if(product.__product_id == product_id):
                return product

    def display_all(self):
        for product in self.__product_list:
            product.display_information()
        