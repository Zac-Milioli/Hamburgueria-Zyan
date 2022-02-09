class Mesa:
    def __init__(self, numero, cliente):
        self.__numero = numero
        self.__cliente = cliente

    @property
    def get_numero(self):
        """Retorna numero"""
        return self.__numero

    @numero.setter
    def set_numero(self, numero):
        """Altera numero"""
        self.__numero = numero
        return self.__numero

    @property
    def get_cliente(self):
        """Retorna cliente"""
        return self.__cliente

    @cliente.setter
    def set_cliente(self, cliente):
        """Altera cliente"""
        self.__cliente = cliente
        return self.__cliente
    