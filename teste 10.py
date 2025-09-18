while True:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    print(f'Olá {nome}! sua idade é {idade} anos.')

    if idade >= 18:
        print('Você é maior de idade!')
    else:
        print('Você é menor de idade!')

    pergunta = input(f'{nome} você possui documento de identidade? (sim/não): ')
    if pergunta.lower() == 'sim':
        print('Ótimo! Você tem todos os documentos necessários!')
    else:
        print('Você precisa regularizar sua documentação')

    continuar = input('Deseja realizar o cadastro novamente? (sim/não): ')
    if continuar.lower() != 'sim':    
        print('Obrigado por usar o programa!')
        break            