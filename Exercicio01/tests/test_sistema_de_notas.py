from typing import Literal
from Exercicio01.src.sistema_de_notas import validar_nota, calcular_media, obter_situacao,calcular_estatisticas, normalizar_notas
import pytest

# Teste notas válidas
@pytest.mark.parametrize("nota, esperado", [
    (0, True),
    (1, True),
    (2, True),
    (3, True),
    (8, True),
    (9, True),
    (4, True),
    (5, True),
    (6, True),
    (10, True),
])
def test_validar_notas_notas_validas(nota, esperado):
    assert validar_nota(nota) is esperado

#Testes notas inválidas positivas
@pytest.mark.parametrize("nota, esperado", [
    (11, False),
    (22, False),
    (24, False),
    (100, False),
    (15, False),
])
def teste_notas_invalidas_positivas(nota, esperado):
    assert validar_nota(nota) is False

#Teste notas invalidas negativas
@pytest.mark.parametrize("nota, esperado", [
    (-100, False),
    (12, False),
    (200, False),
    (11, False),
    (13, False),
    (141, False),
    (200, False),
    (17, False),
    (22, False),
    (14, False)
])
def test_notas_invalidas_negativas(nota, esperado):
    assert validar_nota(nota) is False

#Teste calcular media valores validos
@pytest.mark.parametrize("nota, esperado", [
    ([1, 2, 3], 2),
    ([3, 2, 1], 2),
    ([5, 5, 5], 5),
    ([10, 10], 10),
    ([0, 0, 0], 0),
    ([7, 8, 9], 8),
    ([4, 6], 5),
    ([2, 4, 6, 8], 5),
    ([1, 3, 5, 7, 9], 5),
    ([10, 0], 5),
    ([6, 6, 6, 6], 6),
    ([8, 9], 8.5),
    ([2, 2, 2, 2, 2], 2),
    ([9, 10, 8], 9),
    ([1, 10], 5.5),
])
def test_calcular_media_valores_validos(nota, esperado):
    assert calcular_media(nota) == esperado

#Teste calcular media lista vazia
@pytest.mark.parametrize("entrada", [
    []])
def test_calcular_media_lista_vazia(entrada):
    with pytest.raises(ValueError):
        calcular_media(entrada)

#Teste calcular media entradas invalidas positivas
@pytest.mark.parametrize("entrada", [
    [12, 13, 22, 24],
    [11],
    [222, 16],
    [20, 30],
    [50, 15],
    [100],
])
def test_calcular_media_entradas_invalidas_positivas(entrada):
    with pytest.raises(ValueError):
        calcular_media(entrada)

#Teste calcular media valores inválidos negativos
@pytest.mark.parametrize("entrada", [
    [-100],
    [-1, -2, -3, -4],
    [-11, -12, -13],
    [-15, -20, -14, -17, -22],
])
def test_calcular_media_invalidos_negativos(entrada):
    with pytest.raises(ValueError):
        calcular_media(entrada)

#Teste obter situacao valores válidos
@pytest.mark.parametrize("nota, esperado", [
    (7, "aprovado"),
    (8, "aprovado"),
    (10, "aprovado"),
    (6.9,"recuperacao"),
    (6, "recuperacao"),
    (5, "recuperacao"),
    (4, "reprovado"),
    (3, "reprovado"),
    (2, "reprovado"),
    (1, "reprovado"),
    (0, "reprovado"),
])
def test_obter_situacao_notas_validas(nota, esperado):
    assert obter_situacao(nota) == esperado

#Teste obter situacao valores inválidos positivos
@pytest.mark.parametrize("nota", [
    20, 11, 15, 20, 30, 18, 100
    ])
def test_obter_situacao_notas_invalidas_positivas(nota):
    with pytest.raises(ValueError):
        obter_situacao(nota)

#Teste obter situacao notas inválidass negativas
@pytest.mark.parametrize("nota", [
    -1, -2, -10, -15, -20, -100, -13
    ])
def test_obter_situacao_notas_invalidas_negativas(nota):
    with pytest.raises(ValueError):
        obter_situacao(nota)

#Teste calcular estatisticas com valores válidos
@pytest.mark.parametrize("notas, esperado", [
    (
        [1, 5, 3, 9, 8, ],
    {
        "media": 5.2,
        "maior": 9,
        "menor": 1,
        "aprovados": 2,
        "recuperacao": 1,
        "reprovados": 2
    }),
    (
        [7, 8, 9, 10],
        {
            "media": 8.5,
            "maior": 10,
            "menor": 7,
            "aprovados": 4,
            "recuperacao": 0,
            "reprovados": 0
        }
    ),
    (
        [0, 1, 2, 3],
        {
            "media": 1.5,
            "maior": 3,
            "menor": 0,
            "aprovados": 0,
            "recuperacao": 0,
            "reprovados": 4
        }
    ),
    (
        [5, 6, 6, 5],
        {
            "media": 5.5,
            "maior": 6,
            "menor": 5,
            "aprovados": 0,
            "recuperacao": 4,
            "reprovados": 0
        }
    ),
    (
        [4, 5, 6, 7],
        {
            "media": 5.5,
            "maior": 7,
            "menor": 4,
            "aprovados": 1,
            "recuperacao": 2,
            "reprovados": 1
        }
    ),
    (
        [0, 0, 10, 10],
        {
            "media": 5,
            "maior": 10,
            "menor": 0,
            "aprovados": 2,
            "recuperacao": 0,
            "reprovados": 2
        }
    ),
    (
        [9],
        {
            "media": 9,
            "maior": 9,
            "menor": 9,
            "aprovados": 1,
            "recuperacao": 0,
            "reprovados": 0
        }
    ),
    (
        [3],
        {
            "media": 3,
            "maior": 3,
            "menor": 3,
            "aprovados": 0,
            "recuperacao": 0,
            "reprovados": 1
        }
    ),
    (
        [3],
        {
            "media": 7,
            "maior": 8,
            "menor": 6,
            "aprovados": 2,
            "recuperacao": 1,
            "reprovados": 0
        }
    ),
    (
        [10, 2, 6, 4, 8],
        {
            "media": 6,
            "maior": 10,
            "menor": 2,
            "aprovados": 2,
            "recuperacao": 1,
            "reprovados": 2
        }
    )
])
def test_calcular_estatisticas_valores_validos(notas, esperado):
    resultado = calcular_estatisticas(notas)

#Testes calcular estatisticas valores invalidos positivos
@pytest.mark.parametrize("notas", [
    [11, 15, 26, 30, 10.5],
    [10.1, 10.2, 15.6],
    [20, 11, 14, 17],
    [100, 200],
    [10.1],
    [10.01],
    [12, 15, 25],
])
def test_calcular_estatisticas_notas_invalidas_positivas(notas):
    with pytest.raises(ValueError):
        calcular_estatisticas(notas)

#Testes calcular estatisticas notaS invalidas negativas
@pytest.mark.parametrize("notas", [
    [-1.9, -2, -3],
    [-10, -11, -12],
    [-5],
    [-20, -100],
    [-1.9, -2.5, -3.1],
    [-20, -14, -16, -15, ],
    [-12, -2, -5, -14],
    [-1]
])
def test_calcular_estatisticas_notas_invalidas_negativas(notas):
    with pytest.raises(ValueError):
        calcular_estatisticas(notas)
#Testes calcular estatisticas notas invalidas positivas e negativas
@pytest.mark.parametrize("notas", [
    [11, 15, -26, 30, -10.5],
    [1-0.1, 10.2, 15.6],
    [20, -11, 14, -17],
    [100, -200],
    [10.1],
    [-10.01],
    [-12, -15, 25],
])
def test_calcular_estatisticas_notas_invalidas(notas):
    with pytest.raises(ValueError):
        calcular_estatisticas(notas)

#Teste normalizar notas validas(entre 0 e 10)
@pytest.mark.parametrize("notas, esperado", [
    ([0], [0.0]),
    ([1], [1.0]),
    ([5], [5.0]),
    ([10], [10.0]),
    ([2], [2.0]),
    ([3], [3.0]),
    ([4], [4.0]),
    ([6], [6.0]),
    ([8], [8.0]),
    ([9], [9.0]),
])
def test_normalizar_notas_validas(notas, esperado):
    assert normalizar_notas(notas) == esperado

#Testes normalizar notas invalidas negativas
@pytest.mark.parametrize("notas", [
    [-1, -6, -9],
    [-2, -15],
    [-3, -18],
    [-4, 5],
    [-1, -5],
    [-100],
    [-20, -22],
])
def test_normalizar_notas_invalidas_negativas(notas):
    with pytest.raises(ValueError):
        normalizar_notas(notas)

#Testes normalizar notas invalidas positivas
@pytest.mark.parametrize("notas", [
    [11, 60, 90],
    [22, 15],
    [13, 18],
    [14, 155, 24.5],
    [10.1, 50],
    [100],
    [20, 22],
])
def test_normalizar_notas_invalidas_positivas(notas):
    with pytest.raises(ValueError):
        normalizar_notas(notas)

#Testes normalizar notas invalidas negativas e positivas
@pytest.mark.parametrize("notas", [
    [-1, -6, 90],
    [-2, 15],
    [-3, 18],
    [14, -5],
    [11, -1.3],
    [10.01, -3],
    [20, -22],
])
def test_normalizar_notas_invalidas_negativas_positivas(notas):
    with pytest.raises(ValueError):
        normalizar_notas(notas)