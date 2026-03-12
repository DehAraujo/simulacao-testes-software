import pytest
from media import media
#from src_mutante.media_mutante1 import media
#from src_mutante.media_mutante2 import media

#Testes media
@pytest.mark.parametrize("numeros, resultado_esperado", [
    ([1, 2, 3], 2),
    ([5, 5, 5], 5),
    ([10, 20], 15),
    ([4, 6, 8, 10], 7),
    ([0, 0, 0], 0),
    ([1, 1, 2], 1.3333333333333333),
    ([2, 4, 6, 8], 5),
    ([100, 200, 300], 200),
    ([3, 6, 9], 6),
    ([7, 14, 21], 14),
])
def test_calcular_media(numeros, resultado_esperado):
    assert media(numeros) == resultado_esperado
    
#Teste lista vazia
@pytest.mark.parametrize("numeros", [
    ([])
])
def test_calcular_media_lista_vazia(numeros):
    with pytest.raises(ValueError):
        media(numeros)

#teste numeros negativos
@pytest.mark.parametrize("numeros", [
    ([-1, -2, -3]),
    ([-5, -5, -5]),
    ([-10, -20]),
    ([-4, -6, -8]),
    ([-2, -4]),
    ([-7, -14, -21]),
    ([-3, -6, -9]),
    ([-1, -3]),
    ([-100, -200, -300]),
    ([-50, -150]),
])
def test_media_negativa(numeros):
    with pytest.raises(ValueError):
        media(numeros)

