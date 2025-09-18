while True:
 nome = input('Digite seu nome: ')
 idade = int(input('Digite sua idade: '))

 print('Olá {}! Você tem {}anos' .format(nome, idade))

 if idade >= 18:
    print('Você é maior de idade!')
 else:
    print('Você é menor de idade!')

 continuar = input('Deseja continuar? (sim/não): ')
 if continuar.lower() != 'sim':
    print('Prgrama encerrado.')
    break