#Importamos a classe Cliente
from cliente import Cliente

#Declaramos o  atributo de lista de pedidos e a classe cliente para a nova classe.
class Pedido:
    def __init__(self):
        self.lista_pedidos = []
        self.cliente = Cliente

#Com essa função, poderemos printar a lista de pedidos existentes

    def print_pedidos(self):
        for pedidos in self.lista_pedidos:
            print("Pedido:", pedidos)


#Função para checarmos se o produto pedido em cardapio existe.
#Inserimos o cliente_pedido e o cardapio.
#Chamaremos a função get_name de cardapio para saber se o item existe em cardapio
#E retornaremos se a informação é verdadeira ou falsa

    def exist_in_cardapio(self, produto, cardapio):
        if cardapio.get_name(produto):
            return True
        return False

#Função final para dizermos se o pedido consta em cardápio ou não.
#Inserimos novamente cliente_pedido e o cardapio existente.
# Chamamos a função exist_in_cardapio para recebermos se a informação é verdadeira ou falsa.
# Se for verdadeira, adicionamos o pedido a lista de pedidos e retornamos uma mensagem como sucesso.
# Se for falso, retornaremos uma mensagem de erro.

    def add_produto(self, pedido, cardapio):
        if self.exist_in_cardapio(pedido, cardapio):
            self.lista_pedidos.append(pedido)
            print("Pedido cadastrado com Sucesso")
        else:
            print('\033[91m' + 'ERRO: Produto não consta em cardápio' + '\033[0m')

