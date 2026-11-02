from product import Product
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
