"""
Metodo burbuja, revisa cada elemento de la lista y los compara con el elemento siguiente de la lista.
Si el elemento es mayor los cambia de posicion

"""


lista = [4,2,6,8,5,7]


print(lista)
for i in range(len(lista)):
    for j in  range(len(lista)-1):
        if lista[j] > lista[j+1]:
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux
            print(lista)
        