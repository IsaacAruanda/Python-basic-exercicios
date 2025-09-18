# Solicitar ao usuário dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Perguntar qual operação o usuário deseja
operacao = input("Escolha a operação (soma, subtração, multiplicação, divisão): ").lower()

# Realizar a operação com base na escolha do usuário
if operacao == "soma":
    resultado = numero1 + numero2
elif operacao == "subtração":
    resultado = numero1 - numero2
elif operacao == "multiplicação":
    resultado = numero1 * numero2
elif operacao == "divisão":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Não é possível dividir por zero."
else:
    resultado = "Operação inválida!"

# Exibir o resultado
print("Resultado:", resultado)
