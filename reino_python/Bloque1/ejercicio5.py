fichero = open("./reino_python/Bloque1/ficheros/mochila.txt", "w", encoding="utf-8")
mochila = ['Antorcha', 'Cuerda de 10 metros', 'Poción de vida', 'Mapa del reino']
for mo in mochila:
    text = mo + '\n'
    fichero.writelines(text)
fichero.close()