# - De menor a mayor o de mayor a menor.
# - Requiere menos comparaciones y es mas eficiente.
# Mas eficiente que el metodo burbuja.


# Busca el elemnto mas pequenioo de la lista
# Lo intercambia por el actual 
# Sigue buscando el dato mas pequenio de la lista
# Intercambia por el actual
# Se repite susecivamente 


lista = [4,2,6,8,5,7,0]

for i in range(len(lista)):
    minimo = i
    # print(minimo)
    for x in range(i, len(lista)):
        if lista[x] < lista[minimo]:
            minimo = x
    
    aux = lista[i]
    lista[i]= lista[minimo]
    lista[minimo] = aux
    print(lista)

print(lista)
