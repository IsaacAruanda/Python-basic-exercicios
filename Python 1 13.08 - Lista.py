def lista_de_compras():
    lista = []  # Lista de compras vazia

    while True:
        try:
            item = input("Digite um item para a lista de compras (ou 'fim' para finalizar): ")

            if item.lower() == "fim":  # Se o usuário digitar "fim", o loop é interrompido
                break
            else:
                lista.append(item)  # Adiciona o item na lista

        except ValueError:
            print("Entrada inválida! Tente novamente.")
    
    # Exibe a lista de compras
    print("\nSua lista de compras:")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")

# Chamando a função para iniciar o programa
lista_de_compras()
