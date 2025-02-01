from typing import override
from StrategyPaymentInterface import StrategyPaymentInterface

class StrategyCreditCardPayment(StrategyPaymentInterface):

    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv

    @override
    def pay(self, amount: float):
        print(f"Paid {amount: .2f} using Credit Card {self.card_number[-4:]}")