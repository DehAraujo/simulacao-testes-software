import unittest
from unittest.mock import MagicMock
from src.calculadora import Calculadora

class TestDoubles(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.calc = Calculadora(self.mock_repo)

    def test_mock_salvar_chamado(self):
        self.calc.somar(2, 3)
        self.mock_repo.salvar.assert_called_once()

    def test_mock_argumento(self):
        self.calc.somar(2, 3)
        self.mock_repo.salvar.assert_called_once_with("2 + 3 = 5")

    def test_mock_potencia_bug_corrigido(self):
        self.calc.potencia(2, 3)
        self.mock_repo.salvar.assert_called_with("2 ** 3 = 8")