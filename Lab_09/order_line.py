from product import Product
class OrderLine:
    __product: Product
    __quantity: int

    def __init__(self, product: Product, quantity: int) -> None:
        self.__product = product
        self.__quantity = quantity
        
        if self.__quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

    def calculate_subtotal(self) -> float:
        return self.__product.price * self.__quantity