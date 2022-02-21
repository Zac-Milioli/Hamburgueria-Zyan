from produto import Produto as p
from cliente import Cliente
from cardapio import Cardapio
import os


print('\nRESTAURANTE ZYAN\n')


def exibir_cardapio():
    """Retorna o cardápio formatado e com todos os produtos"""
    print('\n\t\t\t\tCARDÁPIO')
    print('- ' * 40)
    for itens in c.get_cardapio:
        print(itens)
    print('- ' * 40)


def get_comanda(pessoa):
    """Retorna a comanda formatada de um cliente específico"""
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
