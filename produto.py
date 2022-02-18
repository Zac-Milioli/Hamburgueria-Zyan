class Produto:
    def __init__(self, p_nome, descricao, valor):
        self.__p_nome = p_nome
        """Nome do produto"""
        self.__descricao = descricao
        """Descrição do produto"""
        self.__valor = valor
        """Valor do produto (inteiro)"""

    @property
    def get_p_nome(self):
        """Retorna nome do produto"""
        return self.__p_nome

    def set_p_nome(self, p_nome):
        """Altera nome do produto"""
        self.__p_nome = p_nome
        return self.__p_nome

    @property
    def get_descricao(self):
        """Retorna descrição"""
        return self.__descricao

    def set_descricao(self, descricao):
        """Altera descrição"""
        self.__descricao = descricao
        return self.__descricao

    @property
    def get_valor(self):
        """Retorna valor"""
        return self.__valor

    def set_valor(self, valor):
        """Altera o valor"""
        self.__valor = valor
        return self.__valor

    def __repr__(self):
        return f'\n\t\t\t-> {self.__p_nome}\n\t\t\t\tR${self.__valor},00\n{self.__descricao}\n'
