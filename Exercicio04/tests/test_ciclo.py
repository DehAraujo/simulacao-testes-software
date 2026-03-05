import pytest
from src.teste_ciclo import somar_ate

#teste de ciclo
@pytest.mark.parametrize("n, resultado_esperado", [
    (0, 0),
    (1, 1),
    (10, 45),
])
def test_classificar_caminhos_independentes(n, resultado_esperado):
    assert somar_ate(n) == resultado_esperado