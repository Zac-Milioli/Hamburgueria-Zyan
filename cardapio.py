from produto import Produto as prod
import json


class Cardapio:
    def __init__(self):
        self.__lista_produto = []

    def add_produto(self, produto):
        """Adiciona produto novo"""
        self.__lista_produto.append(produto)

    @property
    def get_cardapio(self):
        """Retorna cardápio"""
        return self.__lista_produto


c = Cardapio()
p = prod('Feijão', 'Feijoada show de bola', 20)
c.add_produto(p)
pr = prod('Macarronada', 'Bem show, alho e óleo', 26)
c.add_produto(pr)

print(c.get_cardapio)

print(p.json_form)
print(pr.json_form)
