from produto import Produto
from cardapio import Cardapio
from pedido import Pedido
from cliente import Cliente

c = Cardapio()
p = Pedido()

card_nom = "Hambúrguer"
card_preco = 18.0
card_des  = "Clássico"
cardp = Produto(card_nom, card_preco, card_des)

card_nom1 = "Hambúrguer"
card_preco1 = 15.0
card_des1  = "Siri"
cardp1 = Produto(card_nom1, card_preco1, card_des1)

card_nom2 = "Hambúrguer"
card_preco2 = 19.0
card_des2  = "Frango"
cardp2 = Produto(card_nom2, card_preco2, card_des2)

nome_cli = "Ryan"
cli_cod = "123"
cli_ped = "Refri"

nome_cli2 = "Zac"
cli_cod2 = "212"
cli_ped2 = "Água"

cliente1 = Cliente(nome_cli, cli_cod, cli_ped)
cliente2 = Cliente(nome_cli2, cli_cod2, cli_ped2)


c.set_cardapio(cardp)
c.set_cardapio(cardp1)
c.set_cardapio(cardp2)

print("Olá, o que gostaria de fazer:")
x = int(input("[1] Novo Produto [2] Novo cliente, [3] Novo Pedido: "))
if x == 1:
    a = int(input("Quantos itens iremos adicionar ao cardápio: "))
    i = 0
    while i < a:
        nome = input("Produto: ")
        preco = float(input("Preço: "))
        descricao = input("Descrição: ")
        prod = Produto(nome, preco, descricao)
        c.new_produto(prod)
        i += 1
        c.get_pro()
elif x == 3:
    p.add_produto(cliente1)


#cardp.alterar_nome(" ")
#cardp.alterar_preço(" ")
#cardp.alterar_des(" ")
#c.get_pro()





#mesas = Mesa()
#mesas.inserir_cli(cliente1)
#mesas.inserir_cli(cliente2)
#mesas.listar_cli()


