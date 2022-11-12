
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
                sentenciaSQL= "INSERT INTO PRODUCTOS VALUES(20/11/2022, 15/12/2022,'QATAR','10 NOCHES HOTEL ESCALONETA EN CAPITAL DE QATAR',TRUE, 1725.999, 20, 20/12/2022 15:00:00, 007)"
                data= (T_PROD_FECH_INI, T_PROD_FECH_FIN, T_PROD_NOMBRE, T_PROD_DETALLE, T_PROD_ACTIVO, T_PROD_PRECIO, T_PROD_PORC_RESERVA, T_PROD_FECHA_HORA_RESERVA, T_PROD_ORDEN)

                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                self.conexion.c
            except:
                print("No se pudo concectar a la base de datos")
            

                