import json

class Produto:
    def __init__(self, p_nome, descricao, valor):
        self.__p_nome = p_nome
        self.__descricao = descricao
        self.__valor = valor

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

    @property
    def json_form(self):
        x = {
            "Produto: ": self.__p_nome,
            "Descrição: ": self.__descricao,
            "Valor: ": self.__valor
        }
        return json.dumps(x, indent=3, ensure_ascii=False, separators=('', ' '))
