while True:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    cor_favorita = input('Digite sua cor favorita: ')

    print(f"Olá {nome}! Você tem {idade} anos e sua cor favorita é {cor_favorita}.")

    if cor_favorita == 'azul':
        print("Que legal! Azul é uma cor muito bonita!")
    else:
        print(f"Que interessante! {cor_favorita} é uma cor única!")

        continuar = input('Deseja fornceer novos dados? (sim/não)')
        if continuar.lower() != 'sim':
           print('Encerrando programa!')
           break   
