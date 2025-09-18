while True:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    print(f"Olá, {nome}! Você tem {idade} anos.")

    if idade < 18:
        print('Você ainda é menor de idade!')
    else:
        print('Você já é maior de idade!') 

    continuar = input('deseja realizar o cadastro novamente? (sim/não)')
    if continuar.lower() != 'sim':
        print('Programa encerradio!')
        break       