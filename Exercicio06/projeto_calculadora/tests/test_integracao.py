import unittest
from src.calculadora import Calculadora
from src.repositorio import HistoricoRepositorio

class TestIntegracao(unittest.TestCase):
    def setUp(self):
        self.repo = HistoricoRepositorio()
        self.calc = Calculadora(self.repo)

    def test_operacoes_sequenciais(self):
        self.calc.somar(2, 3)
        self.calc.multiplicar(self.calc.obter_ultimo_resultado(), 4)
        self.calc.dividir(self.calc.obter_ultimo_resultado(), 2)

        self.assertEqual(self.calc.obter_ultimo_resultado(), 10)
        self.assertEqual(self.repo.total(), 3)