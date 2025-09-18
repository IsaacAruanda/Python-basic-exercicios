while True:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    print(f'Olá, {nome}! Você tem {idade} anos.')

    if idade < 18:
        print('Você é menor de idade!')
    else:
        print('Você é maior de idade!')

    pergunta = input('Você estuda? (sim/não): ')

    if pergunta.lower() == 'sim':
        print('Que ótimo! O estudo é muito importante!')
    else:
        print('Nunca é tarde para começar a estudar!')

    continuar = input('Deseja realizar um novo cadastro? (sim/não):')
    
    if continuar.lower() != 'sim':
        print('Ficamos agradecidos pela tentativa!')
        break                