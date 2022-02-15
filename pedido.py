from cliente import Cliente

class Pedido:
    def __init__(self):
        self.lista_Pedidos = []
        self.cliente = Cliente

    def get_produtos(self):
        return self.lista_Pedidos

    def add_produto(self, pedido):
        self.lista_Pedidos.append(pedido)

    def mostrar_ped(self, cardapio):
        if cardapio.get_name(self.lista_Pedidos[0]):
            print("Pedido executado com Sucesso")
        else:
            print("ERRO:Não possuímos este Produto no Momento")