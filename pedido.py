from cliente import Cliente
class Pedido:
    def __init__(self):
        self.lista_Pedidos = []
        self.cliente = Cliente

    def get_produtos(self):
        return self.lista_Pedidos

    def exist_in_cardapio(self, produto, cardapio):
        if cardapio.get_name(produto):
            return True
        return False

    def add_produto(self, pedido, cardapio):
        if self.exist_in_cardapio(pedido, cardapio):
            self.lista_Pedidos.append(pedido)
            print("Pedido cadastrado com Sucesso")
        else:
            print('\033[91m' + 'ERRO: Produto não consta em cardápio' + '\033[0m')

