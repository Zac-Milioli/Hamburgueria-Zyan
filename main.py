from produto import Produto
from cliente import Cliente
from cardapio import Cardapio


def exibir_cardapio():
    print('\nCARDÁPIO')
    print('- '*8)
    for itens in c.get_cardapio:
        print(itens)
    print('- ' * 8)


c = Cardapio()

c1 = Cliente('Ricardo', 4554, '10')
c2 = Cliente('Marcos', 3216, '06')
d = 'Delicioso macarrão, feito com massa caseira, coberto com nosso molho de creme de leite e ovos.'
p1 = Produto('Macarrão ao Molho Branco', d, 32)
d = 'Frango orgânico, com uma crocante crosta, feito em air-fryer, banhado em molho de tomate. Acompanha arroz.'
p2 = Produto('Frango à Parmegiana', d, 35)
c.add_produto(p1)
c.add_produto(p2)

exibir_clientes()
exibir_cardapio()
