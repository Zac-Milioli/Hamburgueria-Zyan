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
