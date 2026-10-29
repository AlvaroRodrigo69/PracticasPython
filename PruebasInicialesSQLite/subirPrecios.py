import sqlite3
miConexion=sqlite3.connect("OtraBase")
cursor=miConexion.cursor()
cursor.execute('''update productos set precio = precio + 5''')
miConexion.commit()
miConexion.close()