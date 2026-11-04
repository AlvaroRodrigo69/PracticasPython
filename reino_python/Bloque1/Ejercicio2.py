fichero=open("./reino_python/Bloque1/ficheros/diario.txt", "rt", encoding="utf-8")
lineas=fichero.readlines()
#print(lineas)#aparece el \n porque son los salto de linea de cada linea guardada en la lista
for linea in lineas:
    print(">>",linea)
fichero.close()