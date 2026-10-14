from perros import Perro

perraLabrador = Perro("Labrador", "Dorado", 30, 4, "hembra")
perroLabrador = Perro("Labrador", "Negro", 32, 5, "macho")
perraCaniche  = Perro("Caniche", "Blanco", 6, 3, "hembra")
perroCaniche  = Perro("Caniche", "Marrón", 8, 2, "macho")
perroBoxer    = Perro("Boxer", "Atigrado", 28, 6, "macho")

# Listas de prueba
lista = [perraLabrador, perroCaniche]
lista2 = [perroLabrador, perraCaniche, perroBoxer]

caniche=perraLabrador.cruzar(perroLabrador)
print(caniche)
print("\n ")

caniche2=Perro.cruzar2(perroCaniche, perraCaniche)
print(caniche2)
print("\n ")

listaHembras=Perro.obtenerHembras(lista, lista2)
for x in listaHembras:
    print(x)
print("\n ")
perroAfin=perraLabrador.obtenerParejaMasAfin(lista2)
print(perroAfin)