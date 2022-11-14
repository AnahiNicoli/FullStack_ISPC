
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

#TERCERA OPERACIÓN DEL CRUD: UPDATE.
def UPDATEValor(self,T_PROD_FECH_INI, T_PROD_FECH_FIN, T_PROD_NOMBRE, T_PROD_DETALLE, T_PROD_ACTIVO, T_PROD_PRECIO, T_PROD_PORC_RESERVA, T_PROD_FECHA_HORA_RESERVA, T_PROD_ORDEN):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= UPDATE PRODUCTOS
                              SET T_PRODUCTO_PRECIO=1750983
                              WHERE 1
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                self.conexion.c
            except:
                print("No se pudo concectar a la base de datos")
            

                
