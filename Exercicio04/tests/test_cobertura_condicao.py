import pytest
from Exercicio04.src.cobertura_condicao import acesso

#Testes caminhos independentes C0, cobertura de ramos C1 e cobertura de condições CC
@pytest.mark.parametrize("idade, membro, resultado_esperado", [
    (20, True, "Permitido"),
    (18, False, "Negado"),
    (17, True, "Negado"),
    (15, False, "Negado"),
])
def test_ciclo(idade, membro, resultado_esperado):
    assert acesso(idade, membro) == resultado_esperado

#Para a cobertura de ramos C1 são necessários dois casos de testes, um para cobrir o ramo verdadeiro e outro para cobrir o ramo falso
#Para a cobertura de condição CC são necessários quatro casos de testes para cobrir todas as condições possíves de cada ramo.
#Eles se diferem, pois C1 cobre apenas o ramo verdadeiro e o ramo falso e CC cobre cada condição do ramo verdadeiro e cada condição do ramo falso.