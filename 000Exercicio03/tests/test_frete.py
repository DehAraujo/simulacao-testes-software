from src.frete import validar_peso, validar_destino, calcular_frete, validar_valor_pedido
import pytest

#Teste classe de equivalência, peso válido
@pytest.mark.parametrize("peso, frete_esperado", [
(0.2, 10.0), #peso menor que 1
(1.5, 15.0), #peso menor que 5
(10.0, 25.0), #peso menor que 20
])
def test_calcular_frete_peso_valido(peso, frete_esperado):
        assert validar_peso(peso) == frete_esperado

#Teste classe de equivalência peso inválido
@pytest.mark.parametrize("peso", [
    (-2.0), #peso negativo
    (0.0), #peso zero
])
def test_calcular_frete_peso_invalido(peso):
        with pytest.raises(ValueError):
            validar_peso(peso)

#Teste classe de equivalência destino válido (por que falha quando retorno None? já que nao tenho retorno?)
@pytest.mark.parametrize("destino", [
    ("mesma_regiao"),
    ("outra_regiao"),
    ("internacional"),
])
def test_validar_destino_com_destino_valido(destino):
    assert validar_destino(destino) == destino

#Teste classe de equivalência destino inválido
@pytest.mark.parametrize("destino", [
    ("sul"),
    ("sudeste1"),
    ("457888"),
    ("-1"),
    ("@@"),
])
def test_validar_destino_com_destino_invalido(destino):
    with pytest.raises(ValueError):
        validar_destino(destino)

#Teste classe de equivalência valor do pedido valido menor 200 e maior que 200
@pytest.mark.parametrize("valor_pedido, valor_esperado", [
    (50.0, 50.0), #valor menor que 200
    (250.0, 0.0), #valor maior que 200
] )
def test_valor_pedido_valido(valor_pedido, valor_esperado):
    assert validar_valor_pedido(valor_pedido) == valor_esperado

#Teste classe de equivalência valor do pedido inválido
@pytest.mark.parametrize("valor_pedido", [
    (-5), #valor negativo
])
def test_valor_pedido_invalido(valor_pedido):
    with pytest.raises(ValueError):
        validar_valor_pedido(valor_pedido)

#Teste valore limite peso válido (O teste inválido tem que ser separado, ja que tenho duas variaveis peso e peso_esperado)
@pytest.mark.parametrize("peso, peso_esperado", [
    (0.9, 10.0),  #teste valor limite 1 válido
    (1.0, 10.0),  #válido
    (1.1, 15.0),  #válido
    (4.9, 15.0),  #teste valor limite 5
    (5.0, 15.0),  #válido
    (5.1, 25.0),  #válido
    (19.9, 25.0), #teste valor limite 20
    (20.0, 25.0)  #válido
])
def test_valor_limite_peso_valido(peso, peso_esperado):
    assert validar_peso(peso) == peso_esperado
        
#Teste valore limite peso inválido
@pytest.mark.parametrize("peso", [
(20.1), #inválido
])
def test_validar_peso_invalido(peso):
    with pytest.raises(ValueError):
        validar_peso(peso)
