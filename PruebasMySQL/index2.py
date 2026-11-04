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
    nombre=input("escribe el nombre del cliente ")
    direccion=input("escribe la direccion del cliente ")
    sql='''insert into clientes(nombre, direccion) values(%s, %s)'''
    valores=(nombre, direccion)
    cursor.execute(sql, valores)
    conexion.commit()
    conexion.close()
except mysql.connector.Error as e:
    print(f"se a producido un error: {e}")