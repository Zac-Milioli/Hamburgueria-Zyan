from produto import Produto
from mesa import Mesa
from cliente import Cliente

x = []

c1 = Cliente('Ricardo', 4554)
c2 = Cliente('Marcos', 3216)

x.append(repr(c1))
x.append(repr(c2))
x_len = len(x)

for i in range(0, x_len):
    print(x[i])
