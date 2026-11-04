try:
    fichero = open("./reino_python/Bloque1/ficheros/misiones.txt", "x", encoding="utf8")
    fichero.write("Misión 1: Rescatar al herrero")
    print("Podemos leer el fichero:", fichero.readable())
    print("Podemos escribir el fichero:", fichero.writable())
    fichero.close()
except FileExistsError as ex:
    print("Ya se ha creado un txt con el mismo nombre, señor:", ex)