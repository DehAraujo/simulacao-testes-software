from estoque import Estoque
import pytest

# RED: teste para adicionar produto
def test_adicionar_produto():
    estoque = Estoque()
    estoque.adicionar_produto("Arroz", 10)
    assert estoque.consultar_quantidade("Arroz") == 10

# RED: adicionar o mesmo produto soma
def test_adicionar_mesmo_produto():
    estoque = Estoque()
    estoque.adicionar_produto("Arroz", 10)
    estoque.adicionar_produto("Arroz", 5)
    assert estoque.consultar_quantidade("Arroz") == 15

# RED: remover produto
def test_remover_produto():
    estoque = Estoque()
    estoque.adicionar_produto("Arroz", 10)
    estoque.remover_produto("Arroz", 5)
    assert estoque.consultar_quantidade("Arroz") == 5

# RED: erro ao remover mais do que existe
def test_remover_mais_que_estoque():
    estoque = Estoque()
    estoque.adicionar_produto("Arroz", 5)

    with pytest.raises(ValueError):
        estoque.remover_produto("Arroz", 10)

# RED: quantidade inválida ao adicionar
def test_adicionar_invalido():
    estoque = Estoque()

    with pytest.raises(ValueError):
        estoque.adicionar_produto("Arroz", 0)

# RED: quantidade inválida ao remover
def test_remover_invalido():
    estoque = Estoque()

    with pytest.raises(ValueError):
        estoque.remover_produto("Arroz", -1)

# RED: consultar produto que não existe
def test_consultar_inexistente():
    estoque = Estoque()
    assert estoque.consultar_quantidade("Feijao") == 0

# RED: listar produtos
def test_listar_produtos():
    estoque = Estoque()
    estoque.adicionar_produto("Arroz", 10)
    estoque.adicionar_produto("Feijao", 5)

    produtos = estoque.listar_produtos()
    assert "Arroz" in produtos
    assert "Feijao" in produtos

# RED: produto mais estocado
def test_produto_mais_estocado():
    estoque = Estoque()
    estoque.adicionar_produto("Arroz", 10)
    estoque.adicionar_produto("Feijao", 20)

    assert estoque.produto_mais_estocado() == "Feijao"

# RED: estoque vazio
def test_mais_estocado_vazio():
    estoque = Estoque()
    assert estoque.produto_mais_estocado() is None