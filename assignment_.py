from abc import ABC, abstractmethod
from functools import wraps
import uuid
from datetime import datetime


class Receipt:
    def __init__(self, amount, method, status):
        self.txn_id = str(uuid.uuid4())[:8]
        self.amount = amount
        self.method = method
        self.status = status
        self.timestamp = datetime.now()

    def __str__(self):
        return (
            f"\n------ RECEIPT ------\n"
            f"Transaction ID : {self.txn_id}\n"
            f"Method         : {self.method}\n"
            f"Amount         : ₹{self.amount}\n"
            f"Status         : {self.status}\n"
            f"Time           : {self.timestamp}\n"
            f"----------------------"
        )



def log_transaction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("\n===================================")
        print("Starting Payment Transaction...")
        result = func(*args, **kwargs)
        print("Transaction Finished.")
        print("===================================\n")
        return result
    return wrapper


class PaymentStrategy(ABC):

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass



class CreditCardPayment(PaymentStrategy):

    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def validate(self):
        return len(self.card_number) == 16 and len(self.cvv) == 3

    def pay(self, amount):
        if self.validate():
            return Receipt(amount, "Credit Card", "SUCCESS")
        return Receipt(amount, "Credit Card", "FAILED")



class PayPalPayment(PaymentStrategy):

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate(self):
        return "@" in self.email and len(self.password) >= 6

    def pay(self, amount):
        if self.validate():
            return Receipt(amount, "PayPal", "SUCCESS")
        return Receipt(amount, "PayPal", "FAILED")



class UPIPayment(PaymentStrategy):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def validate(self):
        return "@" in self.upi_id

    def pay(self, amount):
        if self.validate():
            return Receipt(amount, "UPI", "SUCCESS")
        return Receipt(amount, "UPI", "FAILED")



class NetBankingPayment(PaymentStrategy):

    def __init__(self, bank_name, account_number):
        self.bank_name = bank_name
        self.account_number = account_number

    def validate(self):
        return len(self.account_number) >= 8

    def pay(self, amount):
        if self.validate():
            return Receipt(amount, "Net Banking", "SUCCESS")
        return Receipt(amount, "Net Banking", "FAILED")



class PaymentProcessor:

    _registry = {}

    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    @classmethod
    def register_strategy(cls, key, strategy_class):
        cls._registry[key] = strategy_class

    @classmethod
    def available_methods(cls):
        return list(cls._registry.keys())

    @classmethod
    def create(cls, key, *args):
        if key not in cls._registry:
            raise ValueError("Payment method not registered.")
        return cls._registry[key](*args)

    @log_transaction
    def process_payment(self, amount):
        if self.strategy is None:
            print("No payment strategy selected.")
            return None

        receipt = self.strategy.pay(amount)
        print(receipt)
        return receipt


PaymentProcessor.register_strategy("credit_card", CreditCardPayment)
PaymentProcessor.register_strategy("paypal", PayPalPayment)
PaymentProcessor.register_strategy("upi", UPIPayment)
PaymentProcessor.register_strategy("netbanking", NetBankingPayment)

print("Available Methods:")
print(PaymentProcessor.available_methods())

processor = PaymentProcessor()

upi = PaymentProcessor.create("upi", "aditya@oksbi")
processor.set_strategy(upi)
processor.process_payment(1500)

card = PaymentProcessor.create(
    "credit_card",
    "1234567890123456",
    "123"
)
processor.set_strategy(card)
processor.process_payment(3000)

bank = PaymentProcessor.create(
    "netbanking",
    "State Bank",
    "9876543210"
)
processor.set_strategy(bank)
processor.process_payment(5000)

paypal = PaymentProcessor.create(
    "paypal",
    "user@gmail.com",
    "password123"
)
processor.set_strategy(paypal)
processor.process_payment(2200)


invalid = PaymentProcessor.create("upi", "wrongupi")
processor.set_strategy(invalid)
processor.process_payment(800)