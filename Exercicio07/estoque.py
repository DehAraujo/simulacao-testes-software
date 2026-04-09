class Estoque:
    # GREEN: básico para o estoque existir
    def __init__(self):
        self.produtos = {}

    # GREEN: função para adicionar produto e passar no teste
    def adicionar_produto(self, nome, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade inválida")

        # 🔵 REFACTOR: usei get para facilitar (se não existir, começa com 0)
        self.produtos[nome] = self.produtos.get(nome, 0) + quantidade

    # GREEN: função para remover produto e passar no teste
    def remover_produto(self, nome, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade inválida")

        if nome not in self.produtos or self.produtos[nome] < quantidade:
            raise ValueError("Estoque insuficiente")

        self.produtos[nome] -= quantidade

    # GREEN: função para consultar quantidade
    def consultar_quantidade(self, nome):
        return self.produtos.get(nome, 0)

    # GREEN: função para listar só produtos com quantidade > 0
    def listar_produtos(self):
        return {k: v for k, v in self.produtos.items() if v > 0}

    # GREEN: função para pegar o produto com maior quantidade
    def produto_mais_estocado(self):
        if not self.produtos:
            return None

        return max(self.produtos, key=self.produtos.get)