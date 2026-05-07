import pytest
from Exercicio04.src.teste_completo import analisar

# Teste completo cobrindo casos importantes
@pytest.mark.parametrize("numero, resultado_esperado", [
    ([], "Abaixo"),                  # Caso 1: lista vazia, 0 iterações
    ([4], "Abaixo"),                 # Caso 2: positivo par, total=4 < 10
    ([6, 6], "Acima"),               # Caso 3: positivo par, total=12 > 10
    ([-3], "Abaixo"),                # Caso 4: negativo, total -= 1
    ([5], "Abaixo"),                 # Caso 5: positivo ímpar, continue
    ([2, -1, 5, 8], "Abaixo"),       # Caso 6: várias iterações, total=9 < 10
])
def test_completo_analisar(numero, resultado_esperado):
    assert analisar(numero) == resultado_esperado