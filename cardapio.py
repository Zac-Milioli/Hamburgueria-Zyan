from produto import Produto as prod
import json


class Cardapio:
    def __init__(self):
        self.__lista_obj = []
        self.__lista_produto = []

    def add_produto(self, produto):
        """Adiciona produto novo"""
        self.__lista_obj.append(produto)

    def get_lista(self, position):
        """Retorna item da lista de produtos"""
        return self.__lista_obj[position]

    @property
    def get_itens_cardapio(self):
        """Retorna itens do cardápio"""
        return self.__lista_produto

    def format_produto(self, obj):
        """Formata o objeto para aparecer no cardápio"""
        self.__lista_produto.append(obj.json)
        return self.__lista_produto


c = Cardapio()
p = prod('Feijão', 'Feijoada show de bola', 20)
c.add_produto(p)
pr = prod('Macarronada', 'Bem show, alho e óleo', 26)
c.add_produto(pr)

c.format_produto(p)
c.format_produto(pr)

print(c.get_itens_cardapio)
