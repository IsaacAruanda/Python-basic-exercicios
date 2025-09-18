def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    media = soma / quantidade
    return media

notas = []

while True:
    try:
        nota = float(input("Digite uma nota (ou -1 para sair): "))
        
        if nota == -1:
            break
        
        if 0 <= nota <= 10:  # Verifica se a nota está no intervalo válido
            notas.append(nota)
        else:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
    
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

if len(notas) == 0:
    print("Nenhuma nota foi informada.")
else:
    media = calcular_media(notas)
    print(f"A média das notas é: {media:.2f}")
    
    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")
