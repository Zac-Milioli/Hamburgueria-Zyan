from pedido import Pedido
from cardapio import Cardapio
c = Cardapio()

a = int(input("Itens Cardápio: "))
i = 0
while i < a:
    nome = input("Produto: ")
    preco = float(input("Preço: "))
    descricao = input("Descrição: ")
    prod = Pedido(nome, preco, descricao)
    c.new_pro(nome)
    i += 1

c.get_pro()

#prod.cadastrar()













#nome_cli = "Ryan"
#cli_cod = "123"
#cli_ped = "Refri"

#nome_cli2 = "Zac"
#cli_cod2 = "212"
#cli_ped2 = "Água"

#cliente1 = Cliente(nome_cli, cli_cod, cli_ped)
#cliente2 = Cliente(nome_cli2, cli_cod2, cli_ped2)

#mesas = Mesa()
#mesas.inserir_cli(cliente1)
#mesas.inserir_cli(cliente2)
#mesas.listar_cli()


