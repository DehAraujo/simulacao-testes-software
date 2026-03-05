import pytest
from src.cobertura_condicao import acesso

#Testes caminhos independentes C0, cobertura de ramos C1 e cobertura de condições CC
@pytest.mark.parametrize("idade, membro, resultado_esperado", [
    (20, "True", "Permitido"),
    (15, "False", "Negado"),
    (17, "True", "Negado"),
])
def test_classificar_caminhos_independentes(idade, membro, resultado_esperado):
    assert acesso(idade, membro) == resultado_esperado

#Em C1 são necessarios dois testes pois ele analisa a condicao V ou F
#Em CC são necessários 3 testes pois ele analisa cada condição individualmente 
