while True:
 nome = input('Digite seu nome: ')

 print(f'Olá {nome}! Seja bem-vindo(a)!')

 continuar = input('Deseja repetir a saudação?')
 if continuar.lower() != 'Sim':
  print('Programa encerrado!')
  break