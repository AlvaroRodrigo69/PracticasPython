import mysql.connector
try:
    conexion=mysql.connector.connect(
            user='daw',
            password='clave',
            host="127.0.0.1",
            port=41064,
            database="ordenadores"
        )
    cursor=conexion.cursor()
    sql='''select * from clientes'''
    cursor.execute(sql)
    clientes=cursor.fetchall()
    for datos in clientes:
        print(datos)
    conexion.commit()
    conexion.close()
except mysql.connector.Error as e:
    print(f"se a producido un error: {e}")