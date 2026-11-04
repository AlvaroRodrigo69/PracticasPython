fichero = open("./reino_python/Bloque1/ficheros/mochila.txt", "a", encoding="utf-8")
mochila = ['Escudo de roble', '3 monedas de oro']
for mo in mochila:
    text = mo + '\n'
    fichero.writelines(text)
fichero.close()