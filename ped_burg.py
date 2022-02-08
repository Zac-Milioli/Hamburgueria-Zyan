class Ped_burg:
  def __init__(self, total, num, lis_burg, cliente, numero, lis_adc, num1, n_mesa):
    self.total = total
    self.num = num
    self.lis_burg = lis_burg
    self.cliente = cliente
    self.numero = numero
    self.lis_adc = lis_adc
    self.num1 = num1
    self.n_mesa = n_mesa
  
  def pedido(self):
    #Loop que lê o número do burguer, salva a string em uma lista e soma o total
    for i in range(0, self.num):
      opt_burg = int(input('Número do burguer: '))
      if opt_burg == 1:
        self.lis_burg.append('Clássico......R$16.00')
        self.total += 16
      elif opt_burg == 2:
        self.lis_burg.append('Frango........R$16.00')
        self.total += 16
      elif opt_burg == 3:
        self.lis_burg.append('Siri..........R$18.00')
        self.total += 18
      elif opt_burg == 4:
        self.lis_burg.append('Costela.......R$20.00')
        self.total += 20
      elif opt_burg == 5:
        self.lis_burg.append('Vegano........R$18.00')
        self.total += 18
      else:
        print('OPÇÃO INVÁLIDA, COMECE NOVAMENTE')
  #Mesma coisa que o último loop, exceto que é pra adicional
  def ped_adc(self):
    for i in range(0, self.num1):
      opt_adc = int(input('Número do adicional: '))
      if opt_adc == 1:
        self.lis_adc.append('Molho.........R$2.00')
        self.total += 2
      elif opt_adc == 2:
        self.lis_adc.append('Salada........R$4.00')
        self.total += 4
      elif opt_adc == 3:
        self.lis_adc.append('Batata-frita..R$5.00')
        self.total += 5
      elif opt_adc == 4:
        self.lis_adc.append('Frango-frito..R$8.00')
        self.total += 8
      else:
        print('OPÇÃO INVÁLIDA, COMECE NOVAMENTE')
  #Código pra printar a comanda
  def comanda(self):
    #dez = dez% ou taxa de serviço
    dez = (self.total*0.1)
    print('- '*11)
    print('COMANDA\n')
    #loop para printar os hambúrgueres
    for i in range(0, self.num):
      print(self.lis_burg[i])
    #loop para printar os adicionais
    for i in range(0, self.num1):
      print(self.lis_adc[i])
    #Printar o valor do serviço
    print(f'Serviço.......R${round(dez, 2)}0')
    #Somar o 10% com o total
    self.total += dez
    #printar o total
    print(f'\nValor total: R${self.total}0')
    #printar o cliente, número e mesa
    print(f'\nCliente: {self.cliente.title()}\nNúmero: {self.numero}\nMesa {self.n_mesa}')
    print('- '*11)