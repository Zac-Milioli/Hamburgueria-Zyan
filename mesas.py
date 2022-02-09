class Mesa:
    def __init__(self):
        self.lis_cli = []

    def inserir_cli (self, cliente):
        self.lis_cli.append(cliente)

    def listar_cli (self):
        for cliente in self.lis_cli:
            print(cliente.cli_nome, cliente.cli_cod, cliente.cli_ped)