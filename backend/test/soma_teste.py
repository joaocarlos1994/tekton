from unittest import TestCase


class SomaTeste(TestCase):
    def test_soma(self):
        resultado = soma(1, 2)
        self.assertEqual(3, resultado)

def soma(num1=0, num2=0):
    return num1 + num2