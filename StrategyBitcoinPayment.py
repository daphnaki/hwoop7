from typing import override
from StrategyPaymentInterface import StrategyPaymentInterface

class StrategyBitcoinPayment(StrategyPaymentInterface):

    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    @override
    def pay(self, amount: float):
        print(f"Paid {amount: .2f} using Bitcoin wallet {self.wallet_address[-6:]}")