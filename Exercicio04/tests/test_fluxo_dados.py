import pytest
from Exercicio04.src.fluxo_dados import desconto

def test_desconto_vip():
    assert desconto(100, True) == 80

def test_valor_minimo():
    assert desconto(40, False) == 50

def test_sem_desconto():
    assert desconto(200, False) == 200