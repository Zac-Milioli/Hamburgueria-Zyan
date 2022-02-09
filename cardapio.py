from produto import Produto


class Cardapio(Produto):
    def __init__(self):
        self.rede = []

    def cadastrar(self):
        self.rede.append(self.nome, self.preco, self.descricao)
        return self.rede
