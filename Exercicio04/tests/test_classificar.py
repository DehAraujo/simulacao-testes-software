import pytest
from Exercicio04.src.classificar import classificar

#Testes caminhos independentes C0 e cobertura de ramos C1
@pytest.mark.parametrize("valor, valor_esperado", [
    (150, "Alto"),
    (99, "Medio"),
    (30, "Baixo"),
])
def test_classificar_caminhos_independentes(valor, valor_esperado):
    assert classificar(valor) == valor_esperado

#São necessários 3 caminhos de testes para cobrir todos os ramos de C1
#CT1 (x > 100) cobre o primeiro ramo verdadeiro da condição e encerra a execução com retorno "Alto".
#CT2 (x <= 100 e x > 50) cobre o segundo ramo falso da condicao x > 100 e o segundo ramo da condicção verdadeira x > 50 e encerra a execução com retorno "Medio"
#CT3 (x <= 50) cobre o ramo falso da primeira e segunda condição, alcançando o final de retorno "Baixo"