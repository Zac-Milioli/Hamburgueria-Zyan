#Importamos as classes necessárias.
import sys
from produto import Produto
from cardapio import Cardapio
from pedido import Pedido
from cliente import Cliente


#DECLARAMOS  A CLASSE CARDAPIO.
cardapio = Cardapio()

#instanciamento de produtos para o nosso cardápio.

Prod01 = Produto("Hambúrguer-Classico", 18.0, 122)
Prod02 = Produto("Hambúrguer-de-Siri", 15.0, 234)
Prod03 = Produto("Hambúrguer-de-Frango", 14.0, 312)
Prod04 = Produto("Refri", 5.0, 221)
Prod05 = Produto("Água", 4.0, 100)

#Adicionamos estes itens a classe cardapio.

#Podemos alterar informaçõs já existentes com as funções de .alterar da Classe Produto.
Prod05.alterar_nome("Água-com-Gás")
Prod03.alterar_cod(316)
Prod01.alterar_preco(18.5)


cardapio.add_produto(Prod01)
cardapio.add_produto(Prod02)
cardapio.add_produto(Prod03)
cardapio.add_produto(Prod04)
cardapio.add_produto(Prod05)

#Printamos os itens que existem em cardápio.

print(20 * " _ ")
cardapio.print_produtos()

#Criação de uma Def main para criação de  um loop infinito.

def main():

#Def main printa as opções do sistema e guarda a informação na variavel X.

    print("\nOlá, o que gostaria de fazer:")
    x = int(input("[0] Sair \n[1] Ver cardápio \n[2] Novo Produto: \n[3] Novo cliente:\n"))
    print(20 * " _ ")

#Vamos para def menu levando a variavel X com  o valor desejado.

    menu(x)

def menu(x):
#def menu usa a variavel X que pegamos de def main e nos leva para a função desejada em nosso sistema.
    if x == 0:
        #Caso  a variavel x = 0, o sistema e o loop irá se encerrar.
        sys.exit()
    elif x == 1:
        # Caso  a variavel x = 1, os itens irão aparecer no console.
        cardapio.print_produtos()
    elif x == 2:
        # Caso  a variavel x = 2, iremos para a def novo_produto().
        novo_produto()
    elif x == 3:
        # Caso  a variavel x = 4, iremos para a def novo_cliente().
        novo_cliente()
    else:
# Caso  a variavel x =  N, teremos uma mensagem de erro e seremos levados de volta para a def main.
        print('\033[91m' + 'ERRO: Comando inválido' + '\033[0m')
    main()


def novo_produto():
#Def para registrarmos novos produtos ao nosso cardápio.

    i = 0
    a = int(input("Quantos itens iremos adicionar ao cardápio: "))

#Loop para pegarmos mais de 1 item por vez.
    while i < a:

#Registramos os itens novos com um input.
        nome = input("Produto: ")
        preco = float(input("Preço: "))
        cod = input("Codigo: ")
        prod = Produto(nome, preco, cod)

#Item adicionado ao cardápio
        cardapio.add_produto(prod)
        i += 1
        print(20 * " _ ")
#Voltamos a def main a partir daqui.

def novo_cliente():
    #Def para registramos novos clientes e pedidos.

    i = 0
    b = int(input("Quantos clientes iremos registrar: "))

#Novamente faremos um loop para termos mais de 1 cliente.
    while i < b:

#Declaremos a Classe Pedido.
        pedido = Pedido()

#Registramos os clientes com um input().
        cliente_nome = input("Nome: ")
        cliente_cod = float(input("Cod: "))
        cliente_pedido = input("Pedido: ")

#Usaremos a função de Pedido add_produto() para o pedido do cliente e o cardapio existente no momento.
        pedido.add_produto(cliente_pedido, cardapio)

#instanciamento do objeto cliente com as informaçõs inseridas na classe Pedido.
        Cliente(cliente_nome, cliente_cod, pedido)

#Função para printarmos o pedido registrado.
        pedido.print_pedidos
        i += 1
        print(20 * " _ ")
#Voltamos a def main a partir daqui.
main()
