from discount_strategy import DiscountStrategy
class BulkDiscount(DiscountStrategy):
    __threshold: int
    __amount: int

    def __init__(self, threshold: int, amount: int):
        self.__threshold=threshold
        self.__amount=amount

    def apply(self, total):
        return total - self.__amount if total >= self.__threshold else total