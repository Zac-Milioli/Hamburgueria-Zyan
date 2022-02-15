class Produto:
    def __init__(self, nome, preco, codigo):
        self.nome = nome
        self.preco = preco
        self.codigo = codigo

    def alterar_nome (self, newname):
        self.nome = newname

    def alterar_preco (self, newpreco):
        self.preco = newpreco

    def alterar_cod(self, newcod):
        self.codigo = newcod

