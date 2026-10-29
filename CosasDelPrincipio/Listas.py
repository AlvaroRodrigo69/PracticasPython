def recorre_lista(l):
    for x in l:
        print(x)

lista=["Albacete", 1940, 'goles', 66, True]
#recorre_lista(lista)
#lista.append("adios")
#recorre_lista(lista)
#lista.reverse()
#recorre_lista(lista)
lista.insert(1, "carlos")
recorre_lista(lista)
print("---------")
recorre_lista(lista[1:4])