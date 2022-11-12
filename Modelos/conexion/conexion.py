#Clase encargada de la conexion con la base de datos y su gestión
import mysql.connector

class Conexion:

    con = None
    _host = 'localhost'
    _port = 3306
    _user = 'root'
    _password = 'ContraseñaBBDD'
    _db = 'EASYTRAVEL'

    def _init_(self) -> None:
        try:
            self.con = mysql.connector.connect(
                self._host, 
                self._port, 
                self._user, 
                self._password, 
                self._db       
            )
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!",descripcionError)
    
    def getDatosConexion(self):
        return [self._host, self._port, self._user, self._password, self._db]

    def get_host(self):
        return self._host

    def get_port(self):
        return self._port

    def get_user(self):
        return self._user

    def get_password(self):
        return self._password

    def get_db(self):
        return self._db
    
    def set_host(self, h):
        self._host=h

    def set_port(self, p):
        self._port=p

    def set_user(self, u):
        self._user=u

    def set_password(self, pa):
        self._password=pa

    def set_db(self, d):
        self._db=d