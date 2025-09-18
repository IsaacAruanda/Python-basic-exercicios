while True:
    num = int(input('Digite um valor inteiro: '))

    pergunta = input('Deseja saber se o numero é positivo, negativo ou zero? (sim/não)')
    if pergunta.lower() == 'sim':
        if num >0:
            print(f'O numero {num} é positivo.')
        elif num <0:
            print(f'O numero {num} é negativo.')
        else:
            print('O numero é zero.')

    continuar = input('Deseja verificar outro numero? (sim/não): ')
    if continuar.lower() != 'sim':
        print('Encerrando programa.')
        print('Obriogado por usar o programa!')    
        break                