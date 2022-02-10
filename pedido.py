class Pedido:

    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.rede = []

    def alterar_nome(self, newname):
        self.nome = newname

    def alterar_preco(self, newpreco):
        self.preco = newpreco

    def alterar_des(self, newdes):
        self.descricao = newdes


    def cadastrar(self):
        self.rede.append(self.nome)
        self.rede.append(self.preco)
        self.rede.append(self.descricao)
        return print(','.join(map(str, self.rede)))