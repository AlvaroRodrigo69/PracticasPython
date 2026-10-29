import sqlite3
miConexion=sqlite3.connect("MiBase")
miCursor=miConexion.cursor()
miCursor.execute("select * from productos")
misProductos=miCursor.fetchall()
for producto in misProductos:
    print(f"nombre: {producto[0]} | precio: {producto[1]} | seccion: {producto[2]}")
miConexion.commit()
miConexion.close()