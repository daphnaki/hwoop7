from typing import override
from StrategyPaymentInterface import StrategyPaymentInterface

class StrategyBitPayment(StrategyPaymentInterface):

    def __init__(self, bank_account_number: str):
        self.bank_account_number = bank_account_number

    @override
    def pay(self, amount: float):
        print(f"Paid {amount: .2f} using Bit with Bank Account Number {self.bank_account_number}")