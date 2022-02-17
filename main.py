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

c1 = Cliente('Ricardo', 4554, '10')
c2 = Cliente('Marcos', 3216, '06')
d = 'Delicioso macarrão, feito com massa caseira, coberto com nosso molho de creme de leite e ovos.'
p1 = p('Macarrão ao Molho Branco', d, 32)
d = 'Frango orgânico, com uma crocante crosta, feito em air-fryer, banhado em molho de tomate. Acompanha arroz.'
p2 = p('Frango à Parmegiana', d, 35)
c.add_produto(p1)
c.add_produto(p2)

exibir_cardapio()
c1.add_pedido(p1)
get_comanda(c1)

#########################
