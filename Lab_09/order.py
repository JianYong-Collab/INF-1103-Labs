from order_line import OrderLine
from product import Product
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount
class Order:
    __order_id: str
    __order_lines : list[OrderLine]
    __discount: DiscountStrategy

    def __init__(self, order_id: str, discount: DiscountStrategy = NoDiscount()) -> None:
        self.__order_id = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = sum(order_line.calculate_subtotal() for order_line in self.__order_lines)
        return self.__discount.apply(total)

    def set_discount(self, discount_strategy: DiscountStrategy):
        self.__discount=discount_strategy