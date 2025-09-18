while True:
 nome = input('Digite seu nome: ')
 cidade = input('Digite a cidade que você mora: ')
 idade = int(input('Digite sua idade: '))

 print(f'Olá {nome}! Você tem {idade} anos e mora em {cidade}.')

 if idade <= 18:
     print('Você ainda é de menor!')
 else:
     print('Você é maior de idade!')

 continuar = input('Deseja informar os dados de outra pessoa? (sim/não)')
 if continuar.lower() != 'sim':  
    print("programa encerrado!")
    break      
