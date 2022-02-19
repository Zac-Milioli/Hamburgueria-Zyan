class Cliente:
    def __init__(self, nome, cod, mesa):
        """Objeto cliente, contendo nome, código e mesa"""
        self.__nome = nome
        """Nome do cliente"""
        self.__cod = cod
        """Código do cliente (inteiro)"""
        self.__mesa = mesa
        """Mesa do cliente"""
        self.__total = 0
        """Valor gasto pelo cliente (default = 0)"""
        self.__pedido = []
        """Lista com os objetos produto dentro do consumo do cliente"""

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

    def delete_pedido(self, produto):
        """Deleta um pedido do cliente"""
        self.__pedido.remove(produto)
        self.__total -= produto.get_valor

    @property
    def get_pedido(self):
        """"Retorna o pedido do cliente"""
        return self.__pedido

    def __repr__(self):
        return f'\n\t\tCliente: {self.__nome}\n\t\tCódigo: {self.__cod}\n\t\tMesa: {self.__mesa}\n\t\tTotal: {self.__total},00\n'
