from produto import Produto as p
from cliente import Cliente
from cardapio import Cardapio
import os

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
while 1:
    print('\nRESTAURANTE ZYAN\n')
    print('- '*18)
    print('\n-> Por favor, selecione uma opção:\n')
    print('[1] - Exibir cardápio\n[2] - Exibir comanda de cliente atual\n[3] - Adicionar item ao cardápio\n[4] - Iniciar comanda de um novo cliente\n[5] - Adicionar um pedido ao cliente\nDigite qualquer outra coisa para sair\n')
    opt = int(input('-> '))
    if opt == 1:
        os.system('cls')
        exibir_cardapio()
        input('\n\nPressione ENTER para retornar ao menu...\n')
        os.system('cls')
        continue
    elif opt == 2:
        os.system('cls')
        get_comanda(pessoa)
        input('\n\nPressione ENTER para retornar ao menu...\n')
        os.system('cls')
        continue
    elif opt == 3:
        os.system('cls')
        prod_nome = input('\nDigite o nome do produto: ')
        descricao = input('\nAdicione uma descrição ao produto: ')
        preco = int(input('\nAtribua um preço ao produto: '))
        produto = p(prod_nome, descricao, preco)
        c.add_produto(produto)
        os.system('cls')
        continue
    elif opt == 4:
        os.system('cls')
        name = input('\nDigite o nome do cliente: ')
        cod = int(input('\nDigite o cod do cliente: '))
        mesa = input('\nDigite o número da mesa: ')
        pessoa = Cliente(name, cod, mesa)
        pessoa.add_cliente(pessoa)
        os.system('cls')
        continue
    elif opt == 5:
        pessoa.add_pedido(produto)
        os.system('cls')
        continue
    else:
        break
print('\nOBRIGADO POR USAR MEU SISTEMA!  :)\n')
#########################
