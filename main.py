from produto import Produto
from cardapio import Cardapio
from pedido import Pedido
from cliente import Cliente

cardapio = Cardapio()

#instanciamento de itens para o cardápio

Prod01 = Produto("Hambúrguer-Classico", 18.0, 1)
Prod02 = Produto("Hambúrguer-de-Siri", 15.0 , 2)
Prod03 = Produto("Hambúrguer-de-Frango", 14.0 , 3)
Prod04 = Produto("Refri", 5.0, 3)
Prod05 = Produto("Água", 4.0, 4)
cardapio.add_produto(Prod01)
cardapio.add_produto(Prod02)
cardapio.add_produto(Prod03)
cardapio.add_produto(Prod04)
cardapio.add_produto(Prod05)

cardapio.print_produto()

print("\nOlá, o que gostaria de fazer:")
x = int(input("[1] Novo Produto [2] Novo cliente: "))
i = 0
print(20 * " _ ")

if x == 1:
    a = int(input("Quantos itens iremos adicionar ao cardápio: "))
    while i < a:
        nome = input("Produto: ")
        preco = float(input("Preço: "))
        cod = input("Codigo: ")
        prod = Produto(nome, preco, cod)
        cardapio.add_produto(prod)
        i += 1
        cardapio.print_produto()
        print(20*"_")

elif x == 2:
    b = int(input("Quantos clientes iremos registrar: "))
    while i < b:

        pedido = Pedido()
        cliente_nome = input("Nome: ")
        cliente_cod = float(input("Cod: "))
        cliente_pedido = input("Pedido: ")
        pedido.add_produto(cliente_pedido)
        var = Cliente(cliente_nome, cliente_cod, pedido)

        clientes = var.get_cliente_pedido()
        clientes.mostrar_ped(cardapio)
        print(20*"_")

        i += 1
else:
    print("ERRO: Por favor, tente novamente")




