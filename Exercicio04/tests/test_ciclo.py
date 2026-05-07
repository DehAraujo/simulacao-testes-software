import pytest
from Exercicio04.src.teste_ciclo import somar_ate

#teste de ciclo
@pytest.mark.parametrize("n, resultado_esperado", [
    (0, 0),
    (1, 0),
    (10, 45),
])
def test_classificar_caminhos_independentes(n, resultado_esperado):
    assert somar_ate(n) == resultado_esperado