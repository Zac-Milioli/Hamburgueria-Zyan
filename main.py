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
d = 'Bife cru mesmo, pra deixar de ser fresco!'
p1 = p('Bifão', d, 20)
d = 'Somente a fruta, nada além.'
p2 = p('Maçã', d, 5)
d = 'Pra encher linguiça mesmo...'
p3 = p('Linguiça', d, 12)

c.add_produto(p1)
c.add_produto(p2)
c.add_produto(p3)

c1 = Cliente('Marcelo', 256, '02')
c2 = Cliente('Joaquim', 854, '06')
c3 = Cliente('Eren Yeager', 774, '16')

exibir_cardapio()
input('\nPressione ENTER para continuar...')
os.system('cls')

c1.add_pedido(p1)
c1.add_pedido(p2)

get_comanda(c1)
input('\nPressione ENTER para continuar...')
os.system('cls')

c2.add_pedido(p1)
c2.add_pedido(p2)
c2.add_pedido(p3)

get_comanda(c2)
input('\nPressione ENTER para continuar...')
os.system('cls')

c3.add_pedido(p1)

get_comanda(c3)
input('\nPressione ENTER para continuar...')
os.system('cls')

c1.delete_pedido(p2)

get_comanda(c1)
input('\nPressione ENTER para continuar...')
os.system('cls')

c.delete_produto(p3)

exibir_cardapio()
input('\nPressione ENTER para continuar...')
os.system('cls')
#########################
