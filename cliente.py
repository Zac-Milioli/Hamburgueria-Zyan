class Cliente:
    def __init__(self, nome, cod, mesa):
        self.__nome = nome
        self.__cod = cod
        self.__mesa = mesa
        self.__total = 0
        self.__pedido = []

    @property
    def get_nome(self):
        """Retorna nome"""
        return self.__nome

    def set_nome(self, nome):
        """Altera nome"""
        self.__nome = nome
        return self.__nome

    @property
    def get_cod(self):
        """Retorna cod"""
        return self.__cod

    def set_cod(self, cod):
        """Altera cod"""
        self.__cod = cod
        return self.__cod

    @property
    def get_mesa(self):
        """Retorna mesa"""
        return self.__mesa

    def set_numero(self, mesa):
        """Altera mesa"""
        self.__mesa = mesa
        return self.__mesa

    @property
    def get_total(self):
        """Retorna total"""
        return self.__total

    def add_pedido(self, produto):
        """Adiciona objeto produto"""
        self.__pedido.append(produto)
        self.__total += produto.get_valor

    @property
    def get_pedido(self):
        """"Retorna o pedido do cliente"""
        return self.__pedido

    def __repr__(self):
        return f'Cliente: {self.__nome}\nCódigo: {self.__cod}\nMesa: {self.__mesa}'
