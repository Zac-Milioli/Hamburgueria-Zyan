from produto import Produto
from cardapio import Cardapio
from pedido import Pedido
from cliente import Cliente

cardapio = Cardapio()
pedido1 = Pedido()

#instanciamento de itens para o cardápio


Prod01 = Produto("Hambúrguer-Classico", 18.0, 1)
Prod02 = Produto("Hambúrguer-de-Siri", 15.0 , 2)
Prod03 = Produto("Refri", 5.0, 3)

cardapio.add_produto(Prod01)
cardapio.add_produto(Prod02)
cardapio.add_produto(Prod03)

cardapio.print_produto()

#instanciamento de clientes

cli_nome = "Ryan"
cli_cod = "123"
cli_ped = "Hambúrguer-de-Siri"

pedido1.add_produto(cli_ped)
cliente1 = Cliente(cli_nome, cli_cod, pedido1)

# cli_nome2 = "Zac"
# cli_cod2 = "212"
# cli_ped2 = "Água"
# cliente2 = Cliente(cli_nome2, cli_cod2, cli_ped2)


cliente_pedido = cliente1.get_cliente_pedido()
cliente_pedido.mostrar_ped(cardapio)


# print("\nOlá, o que gostaria de fazer:")
# x = int(input("[1] Novo Produto [2] Novo cliente: "))
# i = 0
# if x == 1:
#     a = int(input("Quantos itens iremos adicionar ao cardápio: "))
#     while i < a:
#         nome = input("Produto: ")
#         preco = float(input("Preço: "))
#         cod = input("Codigo: ")
#         prod = Produto(nome, preco, cod)
#         cardapio.new_produto(prod)
#         i += 1
#         cardapio.get_produto()
# elif x == 2:
#     b = int(input("Quantos clientes iremos registrar: "))
#     while i < b:
#         cliente_nome = input("Nome: ")
#         cliente_cod = float(input("Cod: "))
#         cliente_pedido = input("Pedido: ")
#         var = Cliente(cliente_nome, cliente_cod, cliente_pedido)
#         i += 1
# elif x == 3:
#     pedido.add_produto(cliente1)
# else:
#     print("ERRO")
#
#

# Prod01.alterar_nome(" ")
# Prod02.alterar_preço(" ")
# Prod03.alterar_ped(" ")
# cardapio.get_pro()


