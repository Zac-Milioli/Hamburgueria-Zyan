class Produto:
    def __init__(self, nome, preco, codigo):
        self.nome = nome
        self.preco = preco
        self.codigo = codigo

    def alterar_nome (self, newname):
        self.nome = newname
        self.nome = input("Novo Nome: ")

    def alterar_preco (self, newpreco):
        self.preco = newpreco
        self.preco = input("Novo Preço: ")


    def alterar_cod(self, newcod):
        self.descricao = newcod
        self.descricao = input("Novo Cod: ")

