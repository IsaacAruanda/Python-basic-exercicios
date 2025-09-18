while True:
    cor = input('Digite sua cor favorita: ')

    if cor == 'azul':
        print("Azul é uma cor muito bonita!")
    elif cor == 'verde':
        print("Verde é uma cor relaxante!")
    elif cor == 'vermelho':
        print('Vermelho é uma cor cheia de energia!')
    else:
        print('Essa cor tambem é muito interessante!')

    num = int(input('Digite seu numero favorito: '))

    if num <10:
        print('Você prefere números menores!')
    else:
        print('Você prefere numeros maiores')

    continuar = input('Você deseja fazer novamente? (sim/não)')
    if continuar.lower() != 'sim':
        break

