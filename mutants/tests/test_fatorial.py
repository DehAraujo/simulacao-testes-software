import pytest
from fatorial import fatorial
#from src_mutante.fatorial_mutante3 import fatorial
#from src_mutante.fatorial_mutante4 import fatorial

#teste valores válidos
@pytest.mark.parametrize("numero, resultado_esperado", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (10, 3628800),
])
def test_calcular_fatorial_positivo(numero, resultado_esperado):
    assert fatorial(numero) == resultado_esperado

#testes valores invalidos (negativos)
@pytest.mark.parametrize("numero", [
    -1,
    -4,
    -5,
    -7,
    -10
])
def test_calcular_fatorial_negativo(numero):
    with pytest.raises(ValueError):
        fatorial(numero)

