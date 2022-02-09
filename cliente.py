class Cliente:
    def __init__(self, nome, cod, pedido):
        self.__nome = nome
        self.__cod = cod
        self.__pedido = pedido

    @property
    def get_nome(self):
        """Retorna nome"""
        return self.__nome

    @nome.setter
    def set_nome(self, nome):
        """Altera nome"""
        self.__nome = nome
        return self.__nome

    @property
    def get_cod(self):
        """Retorna cod"""
        return self.__cod

    @cod.setter
    def set_cod(self, cod):
        """Altera cod"""
        self.__cod = cod
        return self.__cod

    @property
    def get_pedido(self):
        """Retorna pedido"""
        return self.__pedido

    @pedido.setter
    def set_pedido(self, pedido):
        """Altera pedido"""
        self.__pedido = pedido
        return self.__pedido
