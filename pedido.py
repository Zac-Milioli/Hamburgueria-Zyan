from cliente import Cliente
from cardapio import Cardapio
class Pedido:
    def __init__(self):
        self.lista_Pedidos = []
        self.cliente = Cliente
        self.cardapio = Cardapio()

    def add_produto(self, pedido):
        self.lista_Pedidos.append(pedido)

    def mostrar_ped(self, cliente):
        self.cliente.get_cli_nome(cliente)
        if self.lista_Pedidos == self.cardapio.nomes:
            print("")