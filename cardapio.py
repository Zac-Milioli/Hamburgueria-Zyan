class Cardapio:
    def __init__(self):
        self.produtos = []

    def add_produto(self, produto):
        """Adiciona produto a lista de produtos de cardapio"""
        self.produtos.append(produto)
        return self.produtos

    def get_name(self, name):
        for produto in self.produtos:
            if produto.nome == name:
                return produto
        return False

    def print_produtos(self):
        print("CARDÁPIO")
        for produto in self.produtos:
            print("Nome:",produto.nome,",Preço: R$", produto.preco, ",Codigo:", produto.codigo)


