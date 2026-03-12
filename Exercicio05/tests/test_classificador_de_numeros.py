import pytest
from classificador_de_numeros import classificar
#from src_mutante.classificador_de_numeros_mutante1 import classificar
#from src_mutante.classificador_de_numeros_mutante2 import classificar


@pytest.mark.parametrize("numero, resultado_esperado", [
    (-5, "negativo"),
    (-8, "negativo"),
    (-12, "negativo"),
    (-100, "negativo"),
    (-0.9, "negativo"),
    (-0.1, "negativo"),
    (-10000, "negativo"),
    (0, "zero"),
    (0.0001, "positivo" ),
    (0.01, "positivo"),
    (0.5, "positivo"),
    (1, "positivo"),
    (10000, "positivo"),
    (500, "positivo"),
    (600, "positivo"),
])
def test_classificar_numeros(numero, resultado_esperado):
    assert classificar(numero) == resultado_esperado   
 