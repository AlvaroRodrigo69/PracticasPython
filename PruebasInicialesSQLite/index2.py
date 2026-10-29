import sqlite3
miConexion=sqlite3.connect("OtraBase")
cursor=miConexion.cursor()
#cursor.execute("insert into productos values('balon', 15, 'deportes')")
cursor.execute('''
    create table productos(
    id integer primary key autoincrement,
    nombre varchar(50)unique,
    precio integer,
    seccion varchar(20))
''')
masProductos=[
    ("Camiseta",20,"Moda"),
    ("Lampara",60,"Decoracion"),
    ("Tornilos",1,"Ferreteria")
]
cursor.executemany("insert into productos(nombre, precio, seccion) values(?,?,?)",masProductos)
miConexion.commit()
miConexion.close()