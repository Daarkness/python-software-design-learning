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
 
class PaymentProcessor:
    """
        我们将支付的指责剥离开了之后，也新增了耦合，
        如果我们想要新增另外一个支付类型就会变得很复杂
    """
    def pay_debit(self,order,security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
    def pay_credit(self,order,security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        self.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
p =  PaymentProcessor()

p.pay_credit(order,"0372846")

