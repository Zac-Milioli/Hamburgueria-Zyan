#Classe Cliente, com os atributos de nome, código e pedido para cada um dos clientes.
class Cliente:
    def __init__(self, cliente_nome, cliente_codigo, cliente_pedido):
        self.cliente_nome = cliente_nome
        self.cliente_codigo = cliente_codigo
        self.cliente_pedido = cliente_pedido

#Podemos alterar informaçõs já existentes de clientes com as def que estão abaixo.
    def alterar_cli (self, newcli):
        self.cliente_nome = newcli

    def alterar_cod (self, newcod):
        self.cliente_codigo = newcod

    def alterar_ped(self, newped):
        self.cliente_pedido = newped

#Essas funçõs retornam o nome e o pedido do cliente quando solicitadas.

    def get_cli_nome (self):
        return self.cliente_nome

    def get_cliente_pedido(self):
        return self.cliente_pedido