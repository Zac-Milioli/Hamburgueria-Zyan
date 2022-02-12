from produto import Produto
from cardapio import Cardapio
from pedido import Pedido
from cliente import Cliente


cardapio = Cardapio()
pedido = Pedido()

#instanciamento de itens para o cardápio
NomeProduto = "Hambúrguer"
PrecoProduto = 18.0
CodProduto  = 1
Prod01 = Produto(NomeProduto, PrecoProduto, CodProduto)

NomeProduto1 = "Hambúrguer"
PrecoProduto1 = 15.0
CodProduto1  = 2
Prod02 = Produto(NomeProduto1, PrecoProduto1, CodProduto1)

NomeProduto2= "Refri"
PrecoProduto2= 5.0
CodProduto2 = 3
Prod03 = Produto(NomeProduto2, PrecoProduto2, CodProduto2)


#instanciamento de clientes

cli_nome = "Ryan"
cli_cod = "123"
cli_ped = "Refri"
cliente1 = Cliente(cli_nome, cli_cod, cli_ped)

cli_nome2 = "Zac"
cli_cod2 = "212"
cli_ped2 = "Água"
cliente2 = Cliente(cli_nome2, cli_cod2, cli_ped2)



pedido.add_produto(cli_ped)
pedido.mostrar_ped()






#Adicionando itens ao cardapio

# cardapio.new_produto(Prod01)
# cardapio.new_produto(Prod02)
# cardapio.new_produto(Prod03)
# cardapio.get_pro()
#


# print("Olá, o que gostaria de fazer:")
# x = int(input("[1] Novo Produto [2] Novo cliente, [3] Novo Pedido: "))
# if x == 1:
#     a = int(input("Quantos itens iremos adicionar ao cardápio: "))
#     i = 0
#     while i < a:
#         nome = input("Produto: ")
#         preco = float(input("Preço: "))
#         cod = input("Descrição: ")
#         prod = Produto(nome, preco, cod)
#         cardapio.new_produto(prod)
#         i += 1
#         cardapio.get_pro()
# elif x == 2:
#     b = int(input("Quantos clientes iremos registrar: ")
#     i = 0
#     while i < b:
#         cliente_nome = input("Produto: ")
#         cliente_cod = float(input("Preço: "))
#         prod = Cliente(cli_nome, cli_cod)
#         i += 1
#
# elif x == 3:
#     pedido.add_produto(cliente1)
#
# else:
#     print("ERRO")
#
#
# Prod01.alterar_nome(" ")
# Prod02.alterar_preço(" ")
# Prod03.alterar_cod(" ")
# cardapio.get_pro()


