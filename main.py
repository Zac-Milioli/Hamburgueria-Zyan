from produto import Produto
from mesa import Mesa
from cliente import Cliente
from pedido import Pedido
from cardapio import Cardapio
import json


x = []

c1 = Cliente('Ricardo', 4554)
c2 = Cliente('Marcos', 3216)

m1 = Mesa(12)
m2 = Mesa(15)

print(c1.get_nome)
print(c2.get_nome)
print(c1.get_cod)
print(c2.get_cod)
print(m1.get_numero)
print(m2.get_numero)

c1.set_nome('João')
c1.set_cod(5824)
c2.set_nome('Cleber')
m1.set_numero(16)

print('- '*10)
print('Dados alterados e formatados')
print('- '*10)

x.append(repr(c1))
x.append(repr(c2))
x.append(repr(m1))
x.append(repr(m2))

x_len = len(x)

for i in range(0, x_len):
    print(x[i])


    # def __repr__(self):
    #     """String do cardápio"""
    #     return '- '*15, '\nCARDÁPIO\n', f'{self.__lista_produto}', '\n', '- '*15
