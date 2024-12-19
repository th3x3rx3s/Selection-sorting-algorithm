def selection_sort(lista):
    for x in range(len(lista)):
        minindex = x
        for y in range(x+1, len(lista)):
            if lista[minindex]>lista[y]:
                minindex = y
        lista[x], lista[minindex] = lista[minindex], lista[x]
    return lista