import sqlite3
miConexion=sqlite3.connect("MiBase")
cursor=miConexion.cursor()
cursor.execute("CREATE TABLE productos (nombre_articulo varchar(50), precio integer, seccion varchar(20))")
cursor.close()