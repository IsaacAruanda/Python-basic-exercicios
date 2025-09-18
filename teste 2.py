while True:
    numero = int(input("Digite um número para ver sua tabuada: "))
    
    if numero < 0:
        print("Por favor, escolha um número positivo.")
        continue  # Isso faz o programa voltar para o começo do loop e pedir o número novamente
    
    limite = int(input("Até qual número você deseja ver a tabuada? "))
    
    print(f"\nTabuada do {numero} até {limite}:")
    for i in range(1, limite + 1):
        print(f"{numero} x {i} = {numero * i}")
    
    continuar = input("\nGostaria de fazer outra tabuada? (sim/não): ")
    if continuar.lower() != 'sim':
        print("Programa encerrado.")
        break
