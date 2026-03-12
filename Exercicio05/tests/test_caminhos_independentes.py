import pytest
from src.caminhos_independentes import verificar

#teste caminhos independentes C0
@pytest.mark.parametrize ("valor, resultado_esperado" , [
    (4, "ParPositivo"),
    (3,"ImparPositivo"),
    (-5, "Negativo"),
    (0, "Zero"),
] )
def test_verificar_caminhos_independentes(valor, resultado_esperado):
    assert verificar(valor) == resultado_esperado

