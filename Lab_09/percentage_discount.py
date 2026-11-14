from discount_strategy import DiscountStrategy
class PercentageDiscount(DiscountStrategy):
    __discount: float
    def __init__(self, discount: float):
        self.__discount = (100 - discount)/ 100

    def apply(self, total):
        return total * self.__discount