from StrategyBitcoinPayment import StrategyBitcoinPayment
from StrategyCreditCardPayment import StrategyCreditCardPayment
from StrategyPayPalPayment import StrategyPayPalPayment
from StrategyPaymentInterface import StrategyPaymentInterface
from StrategyBitPayment import StrategyBitPayment

class PaymentContext:

    def __init__(self, strategy: StrategyPaymentInterface):
        self.strategy = strategy

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, new_strategy: StrategyPaymentInterface):
        self.__strategy = new_strategy

    def execute_payment(self, amount):
        self.strategy.pay(amount)


credit_card = StrategyCreditCardPayment("1234-5678-9876-5432", "123")
paypal = StrategyPayPalPayment("user@example.com")
bitcoin = StrategyBitcoinPayment("3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy")
bit = StrategyBitPayment("123-45678")

mobileapp = PaymentContext(credit_card)
mobileapp.execute_payment(180.5)
mobileapp.strategy = paypal
mobileapp.execute_payment(220)
mobileapp.strategy = bitcoin
mobileapp.execute_payment(1050)
mobileapp.strategy = bit
mobileapp.execute_payment(1000)
