class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def alterar_nome (self, newname):
        self.nome = newname
        self.nome = input("Novo Nome: ")

    def alterar_preco (self, newpreco):
        self.preco = newpreco
        self.preco = input("Novo Nome: ")


    def alterar_des(self, newdes):
        self.descricao = newdes
        self.descricao = input("Novo Nome: ")

