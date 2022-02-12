class Cliente:
    def __init__(self,cli_nome, cli_cod, cli_ped):
        self.cli_nome = cli_nome
        self.cli_cod = cli_cod
        self.cli_ped = cli_ped

    def alterar_cli (self, newcli):
        self.cli_nome = newcli

    def alterar_preco (self, newcod):
        self.cli_cod = newcod


    def alterar_des(self, newped):
        self.cli_ped = newped

    def get_cli_nome(self):
        return self.cli_nome