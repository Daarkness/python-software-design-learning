import unittest
from io import StringIO
from unittest.mock import patch
 
from dependency_inversion import Authorizer_Robot

 
 

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