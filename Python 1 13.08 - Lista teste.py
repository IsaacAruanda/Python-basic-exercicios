def lista_de_camisas(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

print(lista_de_camisas(1))
print(lista_de_camisas(2))


