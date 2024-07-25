import mysql.connector
from CRUD import read

def buscar_persona(cursor, dni):
    if type(dni) != int:
        return 0
    else:
        return read(cursor, "*", "persona", f"where dni = {dni}")


cnx = mysql.connector.connect(user='root', database='db_example') #root es el usuario por defecto
cursor = cnx.cursor()

print(buscar_persona(cursor, "Eso"))

cursor.close()
cnx.close()

