def lista_de_frutas():
    lista = []

    while True:
        frutas = input('Digite suas frutas (ou "fim" para finalizar): ')
        
        if frutas == 'fim':
            break
        else:
            lista.append(frutas)

    if lista:
        print('\nSua lista de frutas:')
        for i, frutas in enumerate(lista, start=1):
            print(f'{i}. {frutas}')
    else:
        print('Não possui nenhuma fruta na lista.')

lista_de_frutas()
