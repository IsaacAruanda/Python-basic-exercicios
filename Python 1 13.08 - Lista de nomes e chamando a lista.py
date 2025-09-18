def lista_de_nomes():
    lista = []

    while True:
        nomes = input('Digite um nome para a lista de nomes (ou "fim" para finalizar): ')
        
        if nomes.lower() == 'fim':  # Verifica se o usuário digitou 'fim'
            break
        else:
            lista.append(nomes)  # Adiciona o nome à lista
    
    # Exibe a lista de nomes
    if lista:  # Verifica se a lista não está vazia
        print("\nSua lista de nomes:")
        for i, nome in enumerate(lista, start=1):
            print(f"{i}. {nome}")
    else:
        print("Nenhum nome foi adicionado à lista.")

# Chama a função
lista_de_nomes()
