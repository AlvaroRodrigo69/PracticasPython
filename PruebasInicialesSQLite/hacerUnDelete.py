import sqlite3
miConexion=sqlite3.connect("OtraBase")
cursor=miConexion.cursor()
cursor.execute('''delete from productos where id=1''')
miConexion.commit()
miConexion.close()