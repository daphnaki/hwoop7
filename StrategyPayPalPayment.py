
from typing import override
from StrategyPaymentInterface import StrategyPaymentInterface

class StrategyPayPalPayment(StrategyPaymentInterface):

    def __init__(self, email: str):
        self.email = email

    @override
    def pay(self, amount: float):
        print(f"Paid {amount: .2f} using PayPal from {self.email}")
