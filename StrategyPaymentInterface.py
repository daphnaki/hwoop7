from abc import ABC, abstractmethod

class StrategyPaymentInterface(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass