#Clase encargada de la conexion con la base de datos
import mysql.connector

class Conexion:

    con = None

    def _init_(self) -> None:
        try:
            self.con = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'ContraseñaBBDD',
                db = 'EASYTRAVEL'
            )
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!",descripcionError)

