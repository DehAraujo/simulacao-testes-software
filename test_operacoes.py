import pytest
from operacoes import *


# =========================
# TESTES CLASSIFICAR
# =========================

@pytest.mark.parametrize("numero, esperado", [
    (-5, "negativo"),
    (0, "zero"),
    (10, "positivo"),
])
def test_classificar(numero, esperado):
    assert classificar(numero) == esperado


# =========================
# TESTES FATORIAL
# =========================

@pytest.mark.parametrize("numero, esperado", [
    (0, 1),
    (1, 1),
    (5, 120),
])
def test_fatorial(numero, esperado):
    assert fatorial(numero) == esperado


@pytest.mark.parametrize("numero", [-1, -5])
def test_fatorial_negativo(numero):
    with pytest.raises(ValueError):
        fatorial(numero)


# =========================
# TESTES MAIOR
# =========================

@pytest.mark.parametrize("a,b,esperado", [
    (5, 2, 5),
    (10, 20, 20),
    (-3, -1, -1),
])
def test_maior(a,b,esperado):
    assert maior(a,b) == esperado


# =========================
# TESTES MEDIA
# =========================

@pytest.mark.parametrize("numeros,esperado", [
    ([1,2,3],2),
    ([5,5,5],5),
])
def test_media(numeros,esperado):
    assert media(numeros) == esperado


def test_media_lista_vazia():
    with pytest.raises(ValueError):
        media([])


# =========================
# TESTES PRIMO
# =========================

@pytest.mark.parametrize("numero,esperado", [
    (2,True),
    (3,True),
    (4,False),
    (9,False),
])
def test_primo(numero,esperado):
    assert primo(numero) == esperado


def test_primo_negativo():
    with pytest.raises(ValueError):
        primo(-5)