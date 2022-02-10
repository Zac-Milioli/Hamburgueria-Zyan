
from produto import Produto
class Cardapio:
    def __init__(self):
        self.pro = []

    def get_pro(self):
        for i in self.pro:
            print(i)

    def new_pro (self, nome):
        self.pro.append(nome)