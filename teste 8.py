while True:
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o Segundo valor: '))
    num3 = int(input('Digite o terceiro valor: '))

    soma = num1 + num2 + num3
    print(f'A soma dos números é: {soma}')

    if soma > 20:
        print("A soma dos números é maior que 20!")
    else:
        print('A soma dos números é menor ou igual a 20.')

    continuar = input('Deseja realizar os cálculos novamente? (sim/não): ')
    if continuar.lower() != 'sim':
        print('Programa encerrado!')
        break  
