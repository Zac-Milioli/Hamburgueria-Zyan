class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.rede = []

    def alterar_nome (self, newname):
        self.nome = newname
        self.nome = input("Novo Nome: ")
        return True

    def alterar_preco (self, newpreco):
        self.preco = newpreco
        self.preco = input("Novo Preço: ")
        return True

    def alterar_des(self, newdes):
        self.descricao = newdes
        self.descricao = input("Nova Descrição: ")
        return True

    def cadastrar(self):
        self.rede.append(self.nome)
        self.rede.append(self.preco)
        self.rede.append(self.descricao)
        return print(','.join(map(str, self.rede)))
