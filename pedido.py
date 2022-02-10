class Pedido:
    def __init__(self):
        self.lista_pedido = []



    def get_total_pedido(self, cliente):
        self.lista_pedido.append(cliente)


    def add_produto(self, cliente):
        if cliente:
            print("Ae caraio ")
