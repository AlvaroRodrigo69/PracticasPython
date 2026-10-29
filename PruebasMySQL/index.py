import mysql.connector
try:
    conn = mysql.connector.connect(
        host="127.0.0.1", user="daw", password="clave", database="prueba", port="41064"
    )
    cur = conn.cursor()
    cur.execute("SELECT VERSION()")
    print("la version es:",cur.fetchone())
    conn.close()
except mysql.connector.Error as e:
    print(f"error al conectar: {e}")