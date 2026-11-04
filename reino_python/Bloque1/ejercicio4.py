fichero=open("./reino_python/Bloque1/ficheros/personaje.txt", "w", encoding="utf-8")
fichero.write('''Nombre: Aria Vientoalto\nClase: Exploradora\nNivel: 3\nVida: 42''')
#machaca lo que habia en lugar de duplicarlo
fichero.close()