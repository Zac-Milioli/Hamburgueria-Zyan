class Cliente:
    def __init__(self, nome, cod):
        self.__nome = nome
        self.__cod = cod

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

    def __repr__(self):
        """Retornar objeto em formato string"""
        return(f'Cliente: {self.__nome}\nCódigo: {self.__cod}')
