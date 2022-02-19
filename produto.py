#Classe Produto, com os atributos de nome, preço e código para cada um dos produtos.

class Produto:
    def __init__(self, nome, preco, codigo):
        self.nome = nome
        self.preco = preco
        self.codigo = codigo

#As funções abaixo nos servem para alterar as informaçãos já existentes de um produto.
    def alterar_nome (self, newname):
        self.nome = newname

    def alterar_preco (self, newpreco):
        self.preco = newpreco

    def alterar_cod(self, newcod):
        self.codigo = newcod

