from abc import ABC, abstractmethod


class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order, security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self,security_code) -> None:
        self.security_code =security_code
    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"




class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self,security_code) -> None:
        self.security_code =security_code
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class AliPaymentProcessor(PaymentProcessor):
    def __init__(self,ali_account) -> None:
        self.ali_account =ali_account
    def pay(self, order):
        #阿里支付需要使用的是阿里账号，不是 security_code。而是阿里账号
        print("Processing paypal payment type")
        print(f"Using ali account : {self.ali_account}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = AliPaymentProcessor("213dsafasd")
processor.pay(order)
