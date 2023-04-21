
import mysql.connector

class Conectar():

    def _init_(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'ContraseñaBBDD',
                db = 'EASYTRAVEL'

            )
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!",descripcionError)

#OPERACION DEL CRUD: READ O LEER
def BuscarObjeto(self, PROD_NOMBRE):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "SELECT * from PRODUCTO where nombre like '%A%' "
                cursor.execute(sentenciaSQL)
                resultadoREAD = cursor.fetchall()
                self.conexion.close()
                return resultadoREAD
            except:
                print("No se pudo concectar a la base de datos")
                