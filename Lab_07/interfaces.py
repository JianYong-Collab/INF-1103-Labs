from abc import ABC, abstractmethod
class CanBeShipped:
    @abstractmethod
    def calculate_shipping_cost(self):
        pass