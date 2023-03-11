 
from abc import ABC ,abstractmethod
class Order:
    """
        Order 类承接太多指责，增加功能变得复杂，维护这个类成本也很高
    """
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


"""
将PaymentProcessor作为抽象基类，只要是其子类都必须实现pay方法
如果我们想新增一个支付类型，则新增一个PaymentProcessor的子类
"""

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self,order):
        ...



class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"




order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
p =  DebitPaymentProcessor()

p.pay(order,"0372846")

