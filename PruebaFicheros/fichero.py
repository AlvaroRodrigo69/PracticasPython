fichero=open("./PruebaFicheros/prueba.txt", 'r', encoding="utf-8")

# pimeraLinea=fichero.readline()
# print("Esta es la primera linea: ",pimeraLinea)

# segundaLinea=fichero.readline()
# print("esta es la segunda linea: ",segundaLinea)

# terceraLinea=fichero.readline()
# print("esta es la tecera linea: ", terceraLinea)

# cuartaLinea=fichero.readline()
# print("esta es la cuarta linea: ",cuartaLinea)
todas=fichero.readlines()
print(todas)
fichero.close()