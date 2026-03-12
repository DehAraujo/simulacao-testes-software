import pytest
from src.classificar import classificar

#Testes caminhos independentes C0 e cobertura de ramos C1
@pytest.mark.parametrize("valor, valor_esperado", [
    (150, "Alto"),
    (99, "Medio"),
    (30, "Baixo"),
])
def test_classificar_caminhos_independentes(valor, valor_esperado):
    assert classificar(valor) == valor_esperado

#São necessários 2 testes para cobrir C1 já que a função só possui dois ramos (confuso dúvida)