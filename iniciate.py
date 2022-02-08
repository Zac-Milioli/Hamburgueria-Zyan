import os
from cardapio import Cardapio
from ped_burg import Ped_burg


class sys:
#criação da função que ira dar start no sistema
  def iniciate():
    n_mesa = int(input('Qual mesa estamos servindo? '))
    for i in range(0, n_mesa):
      n_cliente = int(input('Quantos clientes farão pedidos nessa mesa? '))
      for i in range(0, n_cliente):
        os.system('clear')
        cardapio = Cardapio
        print(cardapio())
        cliente = input('\nNome do cliente: ')
        numero = input('Numero do cliente: ')
        total = 0
        lis_burg = []
        lis_adc = []
        os.system('clear')
        cardapio = Cardapio
        print(cardapio())
        num = int(input(f'\nQuantos hambúrgueres o cliente gostaria? '))
        num1 = int(input('Quantos adicionais o cliente gostaria? '))
        aux = Ped_burg(total, num, lis_burg, cliente, numero, lis_adc, num1, n_mesa)
        os.system('clear')
        cardapio = Cardapio
        print(cardapio())
        aux.pedido()
        aux.ped_adc()
        os.system('clear')
        aux.comanda()
        input('Pressione ENTER para continuar')