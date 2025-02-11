from unittest import TestCase
from src.calculator import suma, subtract, divide, multiply

# Para ejecutar estas pruebas tenemos que ejecutar -m unittest

class Test_Calculator(TestCase):

    def test_sum(self):
        assert suma(2,3) == 5

    def test_substract(self):
        assert subtract(10,5) == 5

    def test_divide(self):
        result = divide(4,2)
        expect = 2
        assert result == expect
    
    def test_multiply(self):
        result = multiply(3,5)
        expect = 15
        assert result == expect