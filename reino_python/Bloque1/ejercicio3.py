fichero=open("./reino_python/Bloque1/ficheros/diario.txt", "rt", encoding="utf-8")
linea1=fichero.readline()
print(linea1)
restoDeLineas=fichero.readlines()
print(len(restoDeLineas))
#son 3 elementos porque la pimera linea se a guardado en la linea 1 
#por lo que el cursor del fichero se a movido a la segunda y desde hay es desde donde a empezado a leer las demas lineas
fichero.close()