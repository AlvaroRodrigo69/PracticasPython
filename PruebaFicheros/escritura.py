fichero=open("./PruebaFicheros/prueba.txt", 'a', encoding="utf-8")#la "a" respeta lo que habia antes, la "w" machaca los ficheros, la "x" los crea pero no deja leer y si ya exite lanza excepcion
fichero.write("Hola, esta linea es nueva.\n")
fichero.close()