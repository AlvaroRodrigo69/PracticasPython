""" ## Abrimos el fichero
fichero = open("./reino_python/bloque1/ej8/diario.txt", encoding="utf-8")

## Usamosel metodo Seek para leer desde el caracter que quermos que empiece a leer
fichero.seek(7)
print("Leyendo desde el caracter 7:")
print(fichero.read())

## Y cerramos el fichero
fichero.close() """

## Abrimos el fichero
fichero = open("./reino_python/bloque1/ej8/diario.txt", "r+", encoding="utf-8")

lineas = fichero.readlines()
print(lineas)
fichero.write('\nDía 5: Acepté la misión del herrero')



## Y cerramos el fichero
fichero.close()