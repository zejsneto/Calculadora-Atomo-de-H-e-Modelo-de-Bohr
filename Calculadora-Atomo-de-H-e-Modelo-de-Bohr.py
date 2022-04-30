import math

#1
#Calcular o Raio da Órbita, Velocidade do Elétron na Órbita, Comprimento de Onda de De Broglie do elétron, Energia Cinética, Energia Potêncial, Energia Total
def calc_n():
  n = int(input('Entre o valor de n(1,2,3,4...): ')) 
  raio  = n * n * (5.19*(10**-11))
  velo_orb = (2.187*1000000)/(n)
  comp_broglle = (6.626*(10**-34))/((9.11*(10**-31))*velo_orb)
  cinetica = (13.6)/(n*n)
  potencial = (-27.2)/(n*n)
  total = (-13.6)/(n*n)

  print('\nRaio da órbita do elétron é de: {:.2e} (m).'.format(raio))
  print('Velocidade do elétron na órbita é: {:.2e} (m/s).' .format(velo_orb))
  print('Energia cinética no nível selecionado é: {:.2e} (eV).'.format(cinetica));
  print('Energia potencial no nível selecionado é: {:.2e} (eV).'.format(potencial));
  print('Energia total no nível selecionado é: {:.2e} (eV).'.format(total));
  print('Comprimento de onda de De Broglle do elétron no nível n: {:.2e} (m).\n' .format(comp_broglle))

#2
#Calcular a Energia do Fóton, Comprimento de Onda no Fóton, Frequência do Fóton
def calc_NiNf():
  ni= int(input('Entre o valor de n inicial: '))
  nf= int(input('Entre o valor de n final: '))

  #Calculo energia
  ei=-13.6/(ni**2)
  ef=-13.6/(nf**2)
  e=ef-ei
  if e<0:
    print('\nEnergia do fóton emitido/absorvido pelo átomo de H é: {:.2e} (eV).'.format(e*-1))
  else:
    print('\nEnergia do fóton emitido/absorvido pelo átomo de H é: {:.2e} (eV).'.format(e))

  #Calculo comprimento de onda
  #ALTERAR O #H DEPENDENDO SE ELE PEDE H EM J OU EM EV.S
  #h = 6.63*(10**-34) #J
  h = 0.00000000000000415 #eV.s
  c= 3*10**8
  lamb=h*c/e
  if lamb<0:
    print('Comprimento de onda do fóton emitido/absorvido pelo átomo de H é: {:.2e} (m).'.format(lamb*-1))
  else:
    print('Comprimento de onda do fóton emitido/absorvido pelo átomo de H é: {:.2e} (m).'.format(lamb))

  #Calculo frequencia
  f=e/h
  if f<0:
    print('Frequência do fóton emitido/absorvido pelo átomo de H é: {:.2e} (Hz).\n'.format(f*-1))
  else:
    print('Frequência do fóton emitido/absorvido pelo átomo de H é: {:.2e} (Hz).\n'.format(f))

#3
#Calcular o nível final após um átomo absorver um fóton
def calc_3():
        from math import sqrt
        compriondafoton = 0
        energfoton = 0
        freqfoton = 0
        nivelfinal = 0
        ninicial = 0
        c = 300000000
        #ALTERAR O #H DEPENDENDO SE ELE PEDE H EM J OU EM EV.S
        h = 0.00000000000000415 #eV.s
        #h=6.63*10**-34 #J.s

        print("Deseja calcular o Nf usando como parâmetro: \n1 - Comprimento de Onda Do Fóton(m).\n2 - Frequência Do Fóton(Hz).")
        parametro = int(input("Digite a opção: "))

        if parametro == 1:

          compriondafoton = float(input("Digite o valor do Comprimento de Onda do Fóton(m): "))
          ni = int(input("Digite o valor de n: "))

          ninicial = -13.6/(ni**2)
          energfoton = (h*c)/compriondafoton
          print("\nN inicial: ",ninicial)
          print("Energia do fóton",energfoton)

          nivelfinal = ninicial + (energfoton)
          
          nf = sqrt(-13.6/(nivelfinal))

          print(f"Nível Final após o átomo de H absorver um fóton: {nivelfinal:.2e} (eV)")
          print(f"Nf: {nf:.0e}\n")
          
        elif parametro == 2:

          freqfoton = float(input("Digite o valor da Frequência do Fóton(Hz): "))
          ni = int(input("Digite o valor de n: "))

          ninicial = -13.6/(ni**2)
          energfoton = h*freqfoton
          print("\nN inicial: ",ninicial)
          print("Energia do fóton",energfoton)

          nivelfinal = ninicial + energfoton
          
          nf = sqrt(-13.6/(nivelfinal))

          print(f"Nível Final após o átomo de H absorver um fóton: {nivelfinal:.2e} (eV)")
          print(f"Nf: {nf:.0e} \n")

        else:
          print("\nDado Invalido!\n") 

#4
#Calcular o nível final após um átomo emitir um fóton
def calc_4():
        from math import sqrt
        compriondafoton = 0
        energfoton = 0
        freqfoton = 0
        nivelfinal = 0
        ninicial = 0
        c = 300000000
        #ALTERAR O #H DEPENDENDO SE ELE PEDE H EM J OU EM EV.S
        h = 0.00000000000000415 #eV.s
        #h=6.63*10**-34 #J.s

        print("Deseja calcular o Nf usando como parâmetro: \n1 - Comprimento de Onda Do Fóton(m).\n2 - Frequência Do Fóton(Hz).\n")
        parametro = int(input("Digite a opção:"))

        if parametro == 1:

          compriondafoton = float(input("Digite o valor do Comprimento de Onda do Fóton: "))
          ni = int(input("Digite o valor de n: "))

          ninicial = -13.6/(ni**2)
          energfoton = (h*c)/compriondafoton
          print("\nN inicial: ",ninicial)
          print("Energia do fóton",energfoton)

          nivelfinal = ninicial - (energfoton)

          nf = sqrt(-13.6/(nivelfinal))

          print(f"Nível Final após o átomo de H absorver um fóton: {nivelfinal:.2e} (eV)\n")
          print(f"Nf: {nf:.0e} \n")

        elif parametro == 2:

          freqfoton = float(input("Digite o valor da Frequência do Fóton: "))
          ni = int(input("Digite o valor de n: "))

          ninicial = -13.6/(ni**2)
          energfoton = h*freqfoton
          print("\nN inicial: ",ninicial)
          print("Energia do fóton",energfoton)

          nivelfinal = ninicial - (energfoton)

          nf = sqrt(-13.6/(nivelfinal))

          print(f"Nível Final após o átomo de H absorver um fóton: {nivelfinal:.2e} (eV)\n")
          print(f"Nf: {nf:.0e} \n")

        else:
          print("\nDado Invalido!\n")

#5
#Converter eV para J
def conv_ev():
  ev = float(input('Entre o valor(eV): '))

  j=(ev*(1.60*(10**-19)))
  
  print('\nO valor(eV) convertido para J é: {:.2e} (J).\n'.format(j))

#6
#Converter J para eV
def conv_j():
  j = float(input('Entre o valor(J): '))

  ev=(j/(1.6*(10**(-19))))
  
  print('\nO valor(J) convertido para eV é: {:.2e} (eV).\n'.format(ev))

#7
#Calcular comprimentos de onda a partir de séries
def calc_series():

  R = 10970000 #m-1

  print("Deseja calcular o comprimento de onda usando qual série: \n1 - série de Lyman.\n2 - série de Balmer. \n3 - série de Paschen. \n4 - série de Brackett \n5 - série de Pfund.")
  
  parametro = int(input("Digite a opção: "))

  if parametro == 1:
    n = int(input("Digite o valor de n: "))

    compriOnda = 1/(R*((1/(1**2))-(1/(n**2))))
    
    print(f"\nComprimento de onda da série de Lyman: {compriOnda:.2e}(m)\n")

  elif parametro == 2:
    n = int(input("Digite o valor de n: "))

    compriOnda = 1/(R*((1/(2**2))-(1/(n**2))))
    
    print(f"\nComprimento de onda da série de Balmer: {compriOnda:.2e}(m)\n")

  elif parametro == 3:
    n = int(input("Digite o valor de n: "))

    compriOnda = 1/(R*((1/(3**2))-(1/(n**2))))
    
    print(f"\nComprimento de onda da série de Paschen: {compriOnda:.2e}(m)\n")

  elif parametro == 4:
    n = int(input("Digite o valor de n: "))

    compriOnda = 1/(R*((1/(4**2))-(1/(n**2))))
    
    print(f"\nComprimento de onda da série de Brackett: {compriOnda:.2e}(m)\n")

  elif parametro == 5:
    n = int(input("Digite o valor de n: "))

    compriOnda = 1/(R*((1/(5**2))-(1/(n**2))))
    
    print(f"\nComprimento de onda da série de Pfund: {compriOnda:.2e}(m)\n")

#8
#Calcular a energia do átomo de H no modelo de Bohr
def calc_energia():
  n = (int(input("Digite o valor de n: ")))
  
  en = -13.6/n**2

  print(f"\nO valor da energia do átomo de H no modelo de Bohr é: {en:.2e}(eV)\n")
    
#9
#Imprimir as constantes
def print_const():

  print('\nConstante de Planck(h): 6.63E-34 J.s ou 4.14E-15 eV.s')
  print('Carga elemntar do elétron(e): 1.60E-19 C')
  print('Massa do elétron(me): 9.11E-31 Kg')
  print('Constante de Rydberg(R): 1.097E7 m-1')
  print('Velocidade da luz(c): 3E8 m/s\n')

def main():
  while True:
    print("---***---\n")
    
    print("Escolha uma opção (0 a 9):\n")
    
    print("0 - Encerrar \n")
    
    print("1 - Calcular o Raio da Órbita, Velocidade do Elétron na Órbita, Comprimento de Onda de De Broglie do elétron, Energia Cinética, Energia Potencial, Energia Total\n(Inserir o número quântico(n) do átomo de hidrogênio.)")
    print("2 - Calcular a Energia do Fóton, Comprimento de Onda no Fóton, Frequência do Fóton\n(Inserir o n inicial e o n final do elétron no átomo de H)")
    print("3 - Calcular o nível final após um átomo absorver um fóton\n(Inserindo f ou lambda)")
    print("4 - Calcular o nível final após um átomo emitir um fóton\n(Inserindo f ou lambda)")
    print("5 - Converter eV para J")
    print("6 - Converter J para eV")
    print("7 - Calcular comprimento de onda a partir de séries(Lyman,Balmer,Paschen,Brackett,Pfund)")
    print("8 - Calcular a energia do átomo de H no modelo de Bohr")
    print("9 - Imprimir as constantes\n")
    
    print("---***---\n")
    
    seletor = int(input("Digite a opção: "))
    if (seletor == 1):
      calc_n()
    if (seletor == 2):
      calc_NiNf()
    if (seletor == 3):
      calc_3()
    if (seletor == 4):
      calc_4()
    if (seletor == 5):
      conv_ev()
    if (seletor == 6):
      conv_j()
    if (seletor == 7):
      calc_series()
    if (seletor == 8):
      calc_energia()
    if (seletor == 9):
      print_const()
    elif(seletor==0):
      break
      
main()