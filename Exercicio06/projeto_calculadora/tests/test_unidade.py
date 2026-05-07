import unittest
from unittest.mock import MagicMock
from src.calculadora import Calculadora

class TestUnidade(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_soma(self):
        self.assertEqual(self.calc.somar(2, 3), 5)

    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(5, 2), 3)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_potencia(self):
        self.assertEqual(self.calc.potencia(2, 3), 8)

    def test_divisao_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    def test_tipo_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.somar("a", 2)