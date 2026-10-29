import sqlite3
miConexion=sqlite3.connect("MiBase")
cursor=miConexion.cursor()
#cursor.execute("insert into productos values('balon', 15, 'deportes')")
masProductos=[
    ("Camiseta",20,"Moda"),
    ("Lampara",60,"Decoracion"),
    ("Tornilos",1,"Ferreteria")
]
cursor.executemany("insert into productos values(?,?,?)",masProductos)
miConexion.commit()
miConexion.close()