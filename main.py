import sys
from produto import Produto
from cardapio import Cardapio
from pedido import Pedido
from cliente import Cliente
import pickle

cardapio = Cardapio()
lista_cliente = []


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
print(20 * " _ ")
cardapio.print_produtos()


def main():
    print(20 * " _ ")
    print("\nOlá, o que gostaria de fazer:")
    x = int(input("[-1] Sair \n[0] Ver cardápio \n[1] Novo Produto: \n[2] Novo cliente:\n [3] Ver Clientes "))
    print(20 * " _ ")
    menu(x)

def menu(x):
    if x == -1:
        salve_cliente()
        sys.exit()
    elif x == 0:
        cardapio.print_produtos()
    elif x == 1:
        novo_produto()
    elif x == 2:
        novo_cliente()
    elif x == 3:
        for cliente in lista_cliente:
            print("nome: " + cliente.cli_nome)
    else:
        print('\033[91m' + 'ERRO: Comando inválido' + '\033[0m')
    main()

def novo_produto():
    i = 0
    a = int(input("Quantos itens iremos adicionar ao cardápio: "))
    while i < a:
        nome = input("Produto: ")
        preco = float(input("Preço: "))
        cod = input("Codigo: ")
        prod = Produto(nome, preco, cod)
        cardapio.add_produto(prod)
        i += 1
        print(20 * " _ ")
def novo_cliente():
    i = 0
    b = int(input("Quantos clientes iremos registrar: "))
    while i < b:
        pedido = Pedido()
        cliente_nome = input("Nome: ")
        cliente_cod = float(input("Cod: "))
        cliente_pedido = input("Pedido: ")

        pedido.add_produto(cliente_pedido, cardapio)
        novo_cliente = Cliente(cliente_nome, cliente_cod, pedido)
        lista_cliente.append(novo_cliente)
        i += 1
        print(20 * " _ ")

def salve_cliente():
    #Obj = Dic
    save_cliente = []
    for cliente in lista_cliente:
        lista_produtos = []
        for produto in cliente.cliente_pedido.get_produtos():
            lista_produtos.append(produto)
        save_cliente.append({"nome": cliente.cli_nome, "cod": cliente.cli_cod, "lista": lista_produtos})
    arquivo = open("clientes.pkl", "wb")
#Escrever = WriteB
    pickle.dump(save_cliente, arquivo)
    arquivo.close()


#ler  = Read
def puxar_clientes():
    #Dic = obj
    arquivo1 = open("clientes.pkl", "rb")

    lista_salva = pickle.load(arquivo1)
    for cliente in lista_salva:
        pedido_salvo = Pedido()
        for produto in cliente["lista"]:
            pedido_salvo.add_produto(produto, cardapio)
        cli = Cliente(cliente["nome"], cliente["cod"], pedido_salvo)
        lista_cliente.append(cli)

puxar_clientes()
main()
