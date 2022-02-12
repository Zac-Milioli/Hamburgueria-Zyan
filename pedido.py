from cliente import Cliente
class Pedido:
    def __init__(self):
        self.lista_Pedidos = []
        self.cliente = Cliente()


    def add_produto(self, prod):
        self.lista_Pedidos.append(prod)

    def mostrar_ped(self):
        print(self.cliente.get_cli_nome())
