class Cardapio:
    def __init__(self):
        """Objeto cardápio, carregando a lista de produtos"""
        self.__lista_produto = []
        """Lista com os objetos produto"""

    def add_produto(self, produto):
        """Adiciona produto novo"""
        self.__lista_produto.append(produto)

    def delete_produto(self, produto):
        """Deleta um produto do cardápio"""
        self.__lista_produto.remove(produto)

    @property
    def get_cardapio(self):
        """Retorna cardápio"""
        return self.__lista_produto
