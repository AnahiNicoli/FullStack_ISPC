#Creacion, lectura, actualizacion y eliminaciion de datos

# hace uso de la conexion

import Conexion as con


class Crud:
    con = None

    def __init__(self) -> None:
        self.con = con()
    
    #=======================iNSTRUCCION==============================
    def insert_case(self, argument):
        if argument == "TIPOS_DNI": return "INSERT INTO TIPOS_DNI (T_DNI_ACTIVO,T_DNI_DESCRIPCION) VALUES (?,?)"
        elif argument == "TIPOS_USUARIOS": return "INSERT INTO TIPOS_USUARIOS (T_TUS_ACTIVO, T_TUS_DESCRIPCION) VALUES (?,?)"
        elif argument == "USUARIOS": return "INSERT INTO USUARIOS ( T_USU_NOMBRES, T_USU_APELLIDOS, T_USU_FECH_NAC, T_USU_DNI, T_DNI_ID1, T_USU_PASSW, T_USU_NPERFIL, T_TUS_ID1, T_USU_ACTIVO, T_USU_EMAIL, T_USU_CELULAR, T_USU_PUNTAJE) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
        elif argument == "ETAPAS": return "INSERT INTO ETAPAS (T_ETA_ACTIVA, T_ETA_DESCRIPCION) VALUES (?,?)"
        elif argument == "TIPO_ACCIONES": return "INSERT INTO TIPO_ACCIONES (T_TAC_ACTIVO,T_TAC_DESCRIPCION) VALUES (?,?)"
        elif argument == "COMBOS": return "INSERT INTO COMBOS (T_COMB_FECH_INI, T_COMB_FECH_FIN, T_COMB_PRECIO, T_COMB_NOMBRE, T_COMB_DETALLE,T_COMB_ACTIVO,T_COMB_PORC_RESERVA,T_COMB_FECHA_HORA_RESERVA) VALUES (?,?,?,?,?,?,?,?)"
        elif argument == "NIVELES_PRODUCTOS": return "INSERT INTO NIVELES_PRODUCTOS (T_NIV_ACTIVO,T_NIV_DESCRIPCION) VALUES (?,?)"
        elif argument == "PRODUCTOS" : return "INSERT INTO PRODUCTOS (T_PROD_FECH_INI,T_PROD_FECH_FIN,T_PROD_NOMBRE,T_PROD_DETALLE,T_PROD_ACTIVO,T_NIV_ID1,T_PROD_PRECIO,T_PROD_PORC_RESERVA,T_PROD_FECHA_HORA_RESERVA,T_PROD_ORDEN) VALUES (?,?,?,?,?,?,?,?,?,?)"
        elif argument == "ACCIONES": return "INSERT INTO ACCIONES (T_ACC_FECH_HORA, T_ACC_COMBO_PROD, T_USU_ID1, T_TAC_ID1, T_ETA_ID1,T_COMB_ID3,T_PROD_ID3) VALUES (?,?,?,?,?,?,?)"
        elif argument == "CATEGORIAS": return "INSERT INTO CATEGORIAS (T_CAT_ACTIVA, T_CAT_NOMBRE, T_CAT_ORDEN) VALUES (?,?,?)"
        elif argument == "SUBCATEGORIAS": return "INSERT INTO SUBCATEGORIAS (T_SUB_ACTIVA, T_SUB_NOMBRE, T_SUB_ORDEN) VALUES (?,?,?)"
        elif argument == "PUBLICIDADES": return "INSERT INTO PUBLICIDADES (T_PUB_ACTIVA, T_PUB_FECH_INI, T_PUB_FECH_FIN, T_PUB_DETALLE VALUES (?,?,?,?)"
        elif argument == "EMPRESAS": return "INSERT INTO EMPRESAS (T_PUB_ID1,T_EMP_ACTIVA,T_EMP_NOMBRE,T_EMP_LOGO,T_EMP_DESCRIPCION,T_EMP_ES_ASOCIADA) VALUES (?,?,?,?,?,?)"
        elif argument == "IMAGENES": return "INSERT INTO IMAGENES (T_IMG_IMAGEN) VALUES (?)"
        elif argument == "TIPOS_SERVICIOS": return "INSERT INTO TIPOS_SERVICIOS (T_TSERV_ACTIVO,T_TSERV_NOMBRE) VALUES (?,?)"
        elif argument == "SERVICIOS": return "INSERT INTO SERVICIOS (T_TSERV_ID1,T_SERV_ACTIVO,T_SERV_NOMBRE,T_SERV_DESCRIPCION) VALUES (?,?,?,?,?,?,?,?)"
        elif argument == "COMB_NIV": return "INSERT INTO COMB_NIV (T_COMB_ID1,T_NIV_ID2,T_C_N_ACTIVO) VALUES (?,?,?)"
        elif argument == "COMB_PROD": return "INSERT INTO COMB_PROD (T_COMB_ID2,T_PROD_ID2) VALUES (?,?)"
        elif argument == "CAT_SUB": return "INSERT INTO CAT_SUB (T_CAT_ID1,T_SUB_ID1,T_C_S_ACTIVO) VALUES (?,?,?)"
        elif argument == "CAT_SUB_PROD": return "INSERT INTO CAT_SUB_PROD (T_PROD_ID1,T_C_S_ID1,T_C_S_P_ACTIVO) VALUES (?,?)"
        elif argument == "EMP_SERV": return "INSERT INTO EMP_SERV (T_SERV_ID1,T_EMP_ID1,T_E_S_ACTIVO) VALUES (?,?,?)"
        elif argument == "PUB_IMG": return "INSERT INTO PUB_IMG (T_PUB_ID2,T_IMG_ID1,T_P_I_ACTIVA) VALUES (?,?,?)"
        elif argument == "EMP_SERV_PROD": return "INSERT INTO EMP_SERV_PROD (T_PROD_ID4,T_E_S_ID1,T_E_S_P_ACTIVO) VALUES (?,?,?)"
        pass      
        

    def update_case(self, argument):
        if argument == "TIPOS_DNI": return "UPDATE TIPOS_DNI SET T_DNI_ACTIVO = ? ,T_DNI_DESCRIPCION = ? WHERE T_DNI_ID = ?"
        elif argument == "TIPOS_USUARIOS": return "UPDATE TIPOS_USUARIOS SET T_TUS_ACTIVO = ? , T_TUS_DESCRIPCION = ? WHERE T_TUS_ID = ?"
        elif argument == "USUARIOS": return "UPDATE USUARIOS SET  T_USU_NOMBRES = ? , T_USU_APELLIDOS = ? , T_USU_FECH_NAC = ? , T_USU_DNI = ? , T_DNI_ID1 = ? , T_USU_PASSW = ? , T_USU_NPERFIL = ? , T_TUS_ID1 = ? , T_USU_ACTIVO = ? , T_USU_EMAIL = ? , T_USU_CELULAR = ? , T_USU_PUNTAJE = ? WHERE T_USU_ID = ?"
        elif argument == "ETAPAS": return "UPDATE ETAPAS SET T_ETA_ACTIVA = ? , T_ETA_DESCRIPCION = ? WHERE T_ETA_ID = ?"
        elif argument == "TIPO_ACCIONES": return "UPDATE TIPO_ACCIONES SET T_TAC_ACTIVO = ? ,T_TAC_DESCRIPCION = ? WHERE T_TAC_ID = ?"
        elif argument == "COMBOS": return "UPDATE COMBOS SET T_COMB_FECH_INI = ? , T_COMB_FECH_FIN = ? , T_COMB_PRECIO = ? , T_COMB_NOMBRE = ? , T_COMB_DETALLE = ? ,T_COMB_ACTIVO = ? ,T_COMB_PORC_RESERVA = ? ,T_COMB_FECHA_HORA_RESERVA = ? WHERE T_COMB_ID = ?"
        elif argument == "NIVELES_PRODUCTOS": return "UPDATE NIVELES_PRODUCTOS SET T_NIV_ACTIVO = ? ,T_NIV_DESCRIPCION = ? WHERE T_NIV_ID = ?"
        elif argument == "PRODUCTOS" : return "UPDATE PRODUCTOS SET T_PROD_FECH_INI = ? ,T_PROD_FECH_FIN = ? ,T_PROD_NOMBRE = ? ,T_PROD_DETALLE = ? ,T_PROD_ACTIVO = ? ,T_NIV_ID1 = ? ,T_PROD_PRECIO = ? ,T_PROD_PORC_RESERVA = ? ,T_PROD_FECHA_HORA_RESERVA = ? ,T_PROD_ORDEN = ? WHERE T_PROD_ID = ?"
        elif argument == "ACCIONES": return "UPDATE ACCIONES SET T_ACC_FECH_HORA = ? , T_ACC_COMBO_PROD = ? , T_USU_ID1 = ? , T_TAC_ID1 = ? , T_ETA_ID1 = ? ,T_COMB_ID3 = ? ,T_PROD_ID3 = ? WHERE T_ACC_ID = ?"
        elif argument == "CATEGORIAS": return "UPDATE CATEGORIAS SET T_CAT_ACTIVA = ? , T_CAT_NOMBRE = ? , T_CAT_ORDEN = ? WHERE T_CAT_ID = ?"
        elif argument == "SUBCATEGORIAS": return "UPDATE SUBCATEGORIAS SET T_SUB_ACTIVA = ? , T_SUB_NOMBRE = ? , T_SUB_ORDEN = ? WHERE T_SUB_ID = ?"
        elif argument == "PUBLICIDADES": return "UPDATE PUBLICIDADES SET T_PUB_ACTIVA = ? , T_PUB_FECH_INI = ? , T_PUB_FECH_FIN = ? , T_PUB_DETALLE = ? WHERE T_PUB_ID = ?"
        elif argument == "EMPRESAS": return "UPDATE EMPRESAS SET T_PUB_ID1 = ? ,T_EMP_ACTIVA = ? ,T_EMP_NOMBRE = ? ,T_EMP_LOGO = ? ,T_EMP_DESCRIPCION = ? ,T_EMP_ES_ASOCIADA = ? WHERE T_EMP_ID = ?"
        elif argument == "IMAGENES": return "UPDATE IMAGENES SET T_IMG_IMAGEN = ? WHERE T_IMG_ID = ?"
        elif argument == "TIPOS_SERVICIOS": return "UPDATE TIPOS_SERVICIOS SET T_TSERV_ACTIVO = ? ,T_TSERV_NOMBRE = ? WHERE T_TSERV_ID = ?"
        elif argument == "SERVICIOS": return "UPDATE SERVICIOS SET T_TSERV_ID1 = ? ,T_SERV_ACTIVO = ? ,T_SERV_NOMBRE = ? ,T_SERV_DESCRIPCION = ? WHERE T_COMB_ID1 = ? AND T_NIV_ID2 = ?"
        elif argument == "COMB_NIV": return "UPDATE COMB_NIV SET T_COMB_ID1 = ? ,T_NIV_ID2 = ? ,T_C_N_ACTIVO = ? WHERE T_COMB_ID2 = ? AND T_PROD_ID2 = ?"
        elif argument == "COMB_PROD": return "UPDATE COMB_PROD SET T_COMB_ID2 = ? ,T_PROD_ID2 = ? WHERE T_C_S_ID = ?"
        elif argument == "CAT_SUB": return "UPDATE CAT_SUB SET T_CAT_ID1 = ? ,T_SUB_ID1 = ? ,T_C_S_ACTIVO = ? WHERE T_PROD_ID1 = ? AND T_C_S_ID1 = ?"
        elif argument == "CAT_SUB_PROD": return "UPDATE CAT_SUB_PROD SET T_PROD_ID1 = ? ,T_C_S_ID1 = ? ,T_C_S_P_ACTIVO = ? WHERE T_E_S_ID = ?"
        elif argument == "EMP_SERV": return "UPDATE EMP_SERV SET T_SERV_ID1 = ? ,T_EMP_ID1 = ? ,T_E_S_ACTIVO = ?  WHERE T_PROD_ID = ?"
        elif argument == "PUB_IMG": return "UPDATE PUB_IMG SET T_PUB_ID2 = ? ,T_IMG_ID1 = ? ,T_P_I_ACTIVA = ?  WHERE T_PUB_ID2 = ? AND T_IMG_ID1 = ?"
        elif argument == "EMP_SERV_PROD": return "UPDATE EMP_SERV_PROD SET T_PROD_ID4 = ? ,T_E_S_ID1 = ? ,T_E_S_P_ACTIVO = ?  WHERE T_PROD_ID4 = ? AND T_E_S_ID1 = ?"
        pass      
       

    def selectId_case(self, argument):
        if argument == "TIPOS_DNI": return "SELECT * FROM TIPOS_DNI WHERE T_DNI_ID = ?"
        elif argument == "TIPOS_USUARIOS": return "SELECT * FROM TIPOS_USUARIOS WHERE T_TUS_ID = ?"
        elif argument == "USUARIOS": return "SELECT * FROM USUARIOS WHERE T_USU_ID = ?"
        elif argument == "ETAPAS": return "SELECT * FROM ETAPAS WHERE T_ETA_ID = ?"
        elif argument == "TIPO_ACCIONES": return "SELECT * FROM TIPO_ACCIONES WHERE T_TAC_ID = ?"
        elif argument == "COMBOS": return "SELECT * FROM COMBOS WHERE T_COMB_ID = ?"
        elif argument == "NIVELES_PRODUCTOS": return "SELECT * FROM NIVELES_PRODUCTOS WHERE T_NIV_ID = ?"
        elif argument == "PRODUCTOS" : return "SELECT * FROM PRODUCTOS WHERE T_PROD_ID = ?"
        elif argument == "ACCIONES": return "SELECT * FROM ACCIONES WHERE T_ACC_ID = ?"
        elif argument == "CATEGORIAS": return "SELECT * FROM CATEGORIAS WHERE T_CAT_ID = ?"
        elif argument == "SUBCATEGORIAS": return "SELECT * FROM SUBCATEGORIAS WHERE T_SUB_ID = ?"
        elif argument == "PUBLICIDADES": return "SELECT * FROM PUBLICIDADES WHERE T_PUB_ID = ?"
        elif argument == "EMPRESAS": return "SELECT * FROM EMPRESAS WHERE T_EMP_ID = ?"
        elif argument == "IMAGENES": return "SELECT * FROM IMAGENES WHERE T_IMG_ID = ?"
        elif argument == "TIPOS_SERVICIOS": return "SELECT * FROM TIPOS_SERVICIOS WHERE T_TSERV_ID = ?"
        elif argument == "SERVICIOS": return "SELECT * FROM SERVICIOS WHERE T_COMB_ID1 = ? AND T_NIV_ID2 = ?"
        elif argument == "COMB_NIV": return "SELECT * FROM COMB_NIV WHERE T_COMB_ID2 = ? AND T_PROD_ID2 = ?"
        elif argument == "COMB_PROD": return "SELECT * FROM COMB_PROD WHERE T_C_S_ID = ?"
        elif argument == "CAT_SUB": return "SELECT * FROM CAT_SUB WHERE T_PROD_ID1 = ? AND T_C_S_ID1 = ?"
        elif argument == "CAT_SUB_PROD": return "SELECT * FROM CAT_SUB_PROD WHERE T_E_S_ID = ?"
        elif argument == "EMP_SERV": return "SELECT * FROM EMP_SERV WHERE T_PROD_ID = ?"
        elif argument == "PUB_IMG": return "SELECT * FROM PUB_IMG WHERE T_PUB_ID2 = ? AND T_IMG_ID1 = ?"
        elif argument == "EMP_SERV_PROD": return "SELECT * FROM EMP_SERV_PROD WHERE T_PROD_ID4 = ? AND T_E_S_ID1 = ?"
        pass      

    def max_case(self, argument):
        if argument == "PRODUCTOS": return "SELECT MAX(T_PROD_ID) FROM PRODUCTOS"
        elif argument == "ACCIONES": return "SELECT MAX(T_ACC_ID) FROM ACCIONES WHERE T_ACC_ID = ?"        
        pass      

    def delete_case(self, argument):
        if argument == "TIPOS_DNI": return "DELETE * FROM TIPOS_DNI WHERE T_DNI_ID = ?"
        elif argument == "TIPOS_USUARIOS": return "DELETE * FROM TIPOS_USUARIOS WHERE T_TUS_ID = ?"
        elif argument == "USUARIOS": return "DELETE * FROM USUARIOS WHERE T_USU_ID = ?"
        elif argument == "ETAPAS": return "DELETE * FROM ETAPAS WHERE T_ETA_ID = ?"
        elif argument == "TIPO_ACCIONES": return "DELETE * FROM TIPO_ACCIONES WHERE T_TAC_ID = ?"
        elif argument == "COMBOS": return "DELETE * FROM COMBOS WHERE T_COMB_ID = ?"
        elif argument == "NIVELES_PRODUCTOS": return "DELETE * FROM NIVELES_PRODUCTOS WHERE T_NIV_ID = ?"
        elif argument == "PRODUCTOS" : return "DELETE * FROM PRODUCTOS WHERE T_PROD_ID = ?"
        elif argument == "ACCIONES": return "DELETE * FROM ACCIONES WHERE T_ACC_ID = ?"
        elif argument == "CATEGORIAS": return "DELETE * FROM CATEGORIAS WHERE T_CAT_ID = ?"
        elif argument == "SUBCATEGORIAS": return "DELETE * FROM SUBCATEGORIAS WHERE T_SUB_ID = ?"
        elif argument == "PUBLICIDADES": return "DELETE * FROM PUBLICIDADES WHERE T_PUB_ID = ?"
        elif argument == "EMPRESAS": return "DELETE * FROM EMPRESAS WHERE T_EMP_ID = ?"
        elif argument == "IMAGENES": return "DELETE * FROM IMAGENES WHERE T_IMG_ID = ?"
        elif argument == "TIPOS_SERVICIOS": return "DELETE * FROM TIPOS_SERVICIOS WHERE T_TSERV_ID = ?"
        elif argument == "SERVICIOS": return "DELETE * FROM SERVICIOS WHERE T_COMB_ID1 = ? AND T_NIV_ID2 = ?"
        elif argument == "COMB_NIV": return "DELETE * FROM COMB_NIV WHERE T_COMB_ID2 = ? AND T_PROD_ID2 = ?"
        elif argument == "COMB_PROD": return "DELETE * FROM COMB_PROD WHERE T_C_S_ID = ?"
        elif argument == "CAT_SUB": return "DELETE * FROM CAT_SUB WHERE T_PROD_ID1 = ? AND T_C_S_ID1 = ?"
        elif argument == "CAT_SUB_PROD": return "DELETE * FROM CAT_SUB_PROD WHERE T_E_S_ID = ?"
        elif argument == "EMP_SERV": return "DELETE * FROM EMP_SERV WHERE T_PROD_ID = ?"
        elif argument == "PUB_IMG": return "DELETE * FROM PUB_IMG WHERE T_PUB_ID2 = ? AND T_IMG_ID1 = ?"
        elif argument == "EMP_SERV_PROD": return "DELETE * FROM EMP_SERV_PROD WHERE T_PROD_ID4 = ? AND T_E_S_ID1 = ?"
        pass      
 
#====================CONSULTAS====================
    def insert(self, parameter_list, tabla):
        if self.con.is_connected():
            try:
                cur = self.con.cursor()
                cur.execute(self.insert_case(tabla), parameter_list)
                self.con.commit()   
                cur.close()
                self.con.close() 
            except:
                print("No se pudo concectar a la base de datos")
        pass     
    
    def update(self, parameter_list, tabla):
        if self.con.is_connected():
            try:
                cur = self.con.cursor()
                cur.execute(self.update_case(tabla), parameter_list)
                self.con.commit()    
                cur.close()
                self.con.close()   
            except:
                print("No se pudo concectar a la base de datos") 
        pass    

    def delete(self, id, tabla):
        if self.con.is_connected():
            try:
                cur = self.con.cursor()
                cur.execute(self.delete_case(tabla), [id])
                self.con.commit()   
                cur.close()
                self.con.close() 
            except:
                print("No se pudo concectar a la base de datos")  
        pass       

    def selectId(self, id, tabla):
        if self.con.is_connected():
            try:
                cur = self.con.execute(self.insert_case(tabla), [id])
                data = cur.fetchall() 
                cur.close()
                self.con.close() 
                return data
            except:
                print("No se pudo concectar a la base de datos")
        pass    

    def selectAll(self, tabla, condiciones = None):
        if self.con.is_connected():
            try:
                data = None
                if condiciones == None :
                    cur = self.con.execute("SELECT * FROM " + tabla)
                    data = cur.fetchall() 
                else :
                    cons = "SELECT * FROM " + tabla
                    cons += " WHERE 1 = 1 "
                    for i in range(len(condiciones)):
                        if i%2 == 0:
                            cons += "and " + str(condiciones[i])
                        else :
                            cons += " = " + str(condiciones[i])
                    cur = self.con.execute(cons)
                    data = cur.fetchall() 
                cur.close()
                self.con.close() 
                return data
            except:
                print("No se pudo concectar a la base de datos")
        pass    
    
    def selectMax(self, tabla):
        if self.con.is_connected():
            try:        
                cur = self.con.cursor()
                cur.execute(self.max_case(tabla))
                data = cur.fetchone()[0]
                cur.close()
                self.con.close() 
                return data
            except:
                print("No se pudo concectar a la base de datos")
        pass    


