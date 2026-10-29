import sqlite3
conexion=sqlite3.connect("GestionStock")
cursor=conexion.cursor()
cursor.execute('''
    CREATE TABLE productos(
    codigo varchar(4) primary key,
    nombre varchar(50),
    precio integer,
    seccion varchar(20))
''')
productos=[
    ("CO01","Bañador",22, "Verano"),
    ("CO02","Toalla",15, "Verano"),
    ("CO03", "Manguera",40, "Jardin"),
    ("CO04", "Cubo", 3, "Jardin")
]
cursor.executemany("INSERT INTO productos values(?,?,?,?)", productos)
conexion.commit()
conexion.close()
