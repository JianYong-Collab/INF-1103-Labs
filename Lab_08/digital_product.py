from product import Product
class DigitalProduct(Product):
    __download_size : int

    def __init__(self, product_id, name, price, stock, supplier, download_size) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f" | Download Size: {self.__download_size}")

    def get_fulfilment_info(self) -> None:
        print("This product is delivered digitally")

    def to_dict(self) -> None:
        dict = super().to_dict()
        dict.update({"download_size" : self.__download_size})
        return dict
