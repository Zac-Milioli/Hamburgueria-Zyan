from produto import Produto as p
from cliente import Cliente
from cardapio import Cardapio


def exibir_cardapio():
    print('\n\t\t\t\tCARDÁPIO')
    print('- ' * 40)
    for itens in c.get_cardapio:
        print(itens)
    print('- ' * 40)

def get_comanda(pessoa):
    print('- ' * 40)
    print('\n\t\t\t\tCOMANDA')
    print(pessoa)
    print('\n\tPEDIDOS:')
    for itens in pessoa.get_pedido:
        print(itens)
    print('- ' * 40)


c = Cardapio()


#### ÁREA DO USUÁRIO ####


#########################
