class Mesa:
    def __init__(self, numero):
        self.__numero = numero

    @property
    def get_numero(self):
        """Retorna numero"""
        return self.__numero

    def set_numero(self, numero):
        """Altera numero"""
        self.__numero = numero
        return self.__numero

    def __repr__(self):
        """Retorna objeto em formato string"""
        return f'Mesa: {self.__numero}'
