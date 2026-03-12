import pytest
from src.teste_de_ciclo_aninhado import percorrer_matriz

#teste de ciclo aninhado
@pytest.mark.parametrize("m, n", [
    (0, 0), #0 iterações
    (3, 0), #ignora n
    (1, 5), #1 laco executa uma vez e o outro varios
    (5, 1), #1 laco executa uma vez e o outro varios
    (3, 3),#ambos os lacos executam várias vezes
])
def test_ciclo_aninhado_percorrer_matriz(m, n):
    assert percorrer_matriz(m, n) is None