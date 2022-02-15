class Cliente:
    def __init__(self, cli_nome, cli_cod, cliente_pedido):
        self.cli_nome = cli_nome
        self.cli_cod = cli_cod
        self.cliente_pedido = cliente_pedido

    def alterar_cli (self, newcli):
        self.cli_nome = newcli

    def alterar_cod (self, newcod):
        self.cli_cod = newcod

    def alterar_ped(self, newped):
        self.cliente_pedido = newped

    def get_cli_nome (self):
        return self.cli_nome

    def get_cliente_pedido(self):
        return self.cliente_pedido