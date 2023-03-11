import unittest
from io import StringIO
from unittest.mock import patch
from dependency_injection import *
from dependency_inversion import Authorizer_Robot

 

class PaymentProcessor_TestCase(unittest.TestCase):

    def test_init(self):
        auth = Authorizer_SMS()
        p = PaymentProcessor(auth)
        self.assertEqual(p.authorizer,auth)

    def test_payment_success(self):
        
        auth = Authorizer_SMS()
        auth.generate_sms_code()  
        with patch('builtins.input', return_value=auth.code):
            p = PaymentProcessor(auth)
            order = Order()
            p.pay(order=order)
            self.assertEqual(order.status,"paid")

    def test_payment_fail(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()  

        with patch('builtins.input', return_value='1234567'):
            p = PaymentProcessor(auth)
            order = Order()
            self.assertRaises(Exception,p.pay,order)


class Authorizer_Robot_TastCase(unittest.TestCase):

    def test_init(self):
        r = Authorizer_Robot()
        self.assertEqual(r.authorized,False)

    def test_authorize_success(self):
        r = Authorizer_Robot()
        with patch('builtins.input', return_value="n"):
            r.authorize()
            self.assertTrue(r.is_authorized())

    def test_authorize_fail(self):
        r = Authorizer_Robot()
        with patch('builtins.input', return_value="y"):
            r.authorize()
            self.assertFalse(r.is_authorized())


if __name__ == '__main__':
    unittest.main()