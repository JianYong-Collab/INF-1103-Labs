from discount_strategy import DiscountStrategy
class StudentDiscount(DiscountStrategy):
    __discount: float

    def __init__(self, discount: float):
        self.__discount = discount

    def apply(self, total):
        return total - self.__discount