
class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def alterar_nome (self, newname):
        self.nome = newname
        return True

    def alterar_preco (self, newpreco):
        self.preco =newpreco


    def alterar_des(self, newdes):
        self.descricao = newdes