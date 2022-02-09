from produto import Produto
from cliente import Cliente
from mesas import Mesa

nome = "AAA"
preco = "BBB"
descricao = "CCC"

nome_cli = "Ryan"
cli_cod = "123"
cli_ped = "Refri"

nome_cli2 = "Zac"
cli_cod2 = "212"
cli_ped2 = "Água"

cliente1 = Cliente(nome_cli, cli_cod, cli_ped)
cliente2 = Cliente(nome_cli2, cli_cod2, cli_ped2)

mesas = Mesa()
mesas.inserir_cli(cliente1)
mesas.inserir_cli(cliente2)
mesas.listar_cli()

prod = Produto(nome,preco,descricao)
#prod.alterar_nome(" ")
#prod.cadastrar()
