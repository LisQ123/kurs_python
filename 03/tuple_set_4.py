lista = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24] #podziel liste na 3 rowne elementy i odwroc je
print(lista.reverse())
lista1 = lista[:3]
lista2 = lista[4:7]
lista3 = lista[8:]
print(lista3,"\n", lista2,"\n", lista1)