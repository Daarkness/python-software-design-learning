import string
import random

class Order:
    def __init__(self):
        self.id = ''.join(random.choices(string.ascii_lowercase, k=6))
        self.status = "open"

    def set_status(self, status):
        self.status = status

class Authorizer_SMS:

    def __init__(self):
        self.authorized = False
        self.code = None

    def generate_sms_code(self):
        self.code = ''.join(random.choices(string.digits, k=6))

    def authorize(self):
        code = input("Enter SMS code: ")
        self.authorized = code == self.code

    def is_authorized(self) -> bool:
        return self.authorized

class PaymentProcessor:
    
    def pay(self, order):
        """
            没有办法为pay编写测试用例
            问题在于 pay方法负责创建对象
            我们没有办法在测试用例中创建对象，
            设置一些值，然后传递给pay方法
        """
        authorizer = Authorizer_SMS()
        authorizer.generate_sms_code()
        authorizer.authorize()
        if not authorizer.is_authorized():
            raise Exception("Not authorized")
        print(f"Processing payment for order with id {order.id}")
        order.set_status("paid")
 
        
