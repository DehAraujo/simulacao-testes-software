import pytest
from maior import maior
#from src_mutante.maior_mutante1 import maior
#from src_mutante.maior_mutante2 import maior

#Teste numero maior
@pytest.mark.parametrize("a, b, resultado_esperado", [
    (2, 5, 5),
    (1, 0, 1 ),
    (6, 9, 9),
    (7, 3, 7),
    (0, 2, 2),
    (2, 5, 5),
    (1, 0, 1),
    (10, 3, 10),
    (12, 15, 15),
    (20, 11, 20),
    (30, 40, 40),
    (-2, -5, -2),
    (-15, -10, -10),
    (-20, -30, -20),
    (-50, -25, -25),
    (-3, 5, 5),
    (-2, 5, 5),
    (-1, 3, 3),
    (-6, 9, 9),
    (-10, 2, 2),
    (4, -8, 4),
    (7, 7, 7),
    (5, 5, 5),
    (0, 0, 0),
    (-5, -5, -5),
    (-10, -10, -10),
])
def test_numero_maior(a, b, resultado_esperado):
    assert maior(a, b) == resultado_esperado
