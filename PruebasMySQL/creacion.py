import mysql.connector
try:
    conexion=mysql.connector.connect(
        user='daw',
        password='clave',
        host="127.0.0.1",
        port=41064
    )
    cursor=conexion.cursor()
    cursor.execute("create database ordenadores")
    conexion.close()
except mysql.connector.Error as e:
    print(f"se a producido un error: {e}")

try:
    conexion=mysql.connector.connect(
            user='daw',
            password='clave',
            host="127.0.0.1",
            port=41064,
            database="ordenadores"
        )
    cursor=conexion.cursor()
    sql='''create table clientes(nombre varchar(100), direccion varchar(100))'''
    cursor.execute(sql)
    sql2='''create table empleados(id int auto_increment primary key, nombre varchar(255), puesto varchar(100))'''
    cursor.execute(sql2)
    sql3='''alter table clientes()'''
    conexion.close()
except mysql.connector.Error as e:
    print(f"se a producido un error: {e}")