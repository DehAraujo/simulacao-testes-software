import pytest
from primo import primo
#from src_mutante.primo_mutante1 import primo
#from src_mutante.primo_mutante2 import primo

#Teste numeros primos validos
@pytest.mark.parametrize("numero, resultado_esperado", [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (13, True),
    (17, True),
    (19, True),
    (23, True),
    (29, True),
    (0, False),
    (1, False),
    (4, False),
    (6, False),
    (8, False),
    (9, False),
    (10, False),
    (12, False),
    (14, False),
    (15, False),
])
def test_numeros_primos_validos(numero, resultado_esperado):
    assert primo(numero) == resultado_esperado

#Testes números primos inválidos
@pytest.mark.parametrize("numero", [
    -1,
    -2,
    -3,
    -4,
    -5,
    -7,
    -15,
    -25,
    -100,
    -120,

])
def test_numeros_primos_invalidos(numero):
    with pytest.raises(ValueError):
        primo(numero)
