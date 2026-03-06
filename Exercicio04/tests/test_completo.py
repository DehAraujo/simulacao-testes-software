import pytest
from src.teste_completo import analisar

#teste completo
@pytest.mark.parametrize("numero, resultado_esperado", [

])
def test_completo_analisar(numero, resultado_esperado):
    assert analisar(numero) == resultado_esperado