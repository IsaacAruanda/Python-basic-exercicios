while True:
    nome = input('Digite seu nome: ')
    fruta1 = input('Digite a primeira fruta: ')
    fruta2 =  input('Digite a segunda fruta: ')
    fruta3 = input('Digite a terceira fruta: ')

    print(f"Olá {nome} As frutas que você escolheu são: {fruta1}, {fruta2} e {fruta3}.")

    if fruta1.lower() == 'banana' or fruta2.lower() == 'banana' or fruta3.lower() == 'banana':
       print("Banana é uma fruta deliciosa!")
    else:
        print("Essas são frutas muito boas também!")

    continuar = input('deseja fornecer as frutas novamente? (sim/não)')
    if continuar.lower() != 'sim':
        print('Encerrando programa!')
        break     