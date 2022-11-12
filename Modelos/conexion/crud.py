#Creacion, lectura, actualizacion y eliminaciion de datos

# hace uso de la conexion

import Conexion as con


class Crud:
    con = None

    def __init__(self) -> None:
        self.con = con
    
    #=======================iNSTRUCCION==============================
    def insert_case(self, argument):
        if argument == "PRODUCTOS" : return "INSERT INTO PRODUCTOS (T_PROD_FECH_INI,T_PROD_FECH_FIN,T_PROD_NOMBRE,T_PROD_DETALLE,T_PROD_ACTIVO,T_NIV_ID1,T_PROD_PRECIO,T_PROD_PORC_RESERVA,T_PROD_FECHA_HORA_RESERVA,T_PROD_ORDEN) VALUES (?,?,?,?,?,?,?,?,?,?)"
        elif argument == "NIVELES_PRODUCTOS": return "INSERT INTO NIVELES_PRODUCTOS (T_NIV_ACTIVO,T_NIV_DESCRIPCION) VALUES (?,?)"
        elif argument == "USUARIOS": return "INSERT INTO USUARIOS ( T_USU_NOMBRES, T_USU_APELLIDOS, T_USU_FECH_NAC, T_USU_DNI, T_DNI_ID1, T_USU_PASSW, T_USU_NPERFIL, T_TUS_ID1, T_USU_ACTIVO, T_USU_EMAIL, T_USU_CELULAR, T_USU_PUNTAJE) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
        elif argument == "TIPOS_USUARIOS": return "INSERT INTO TIPOS_USUARIOS (T_TUS_ACTIVO, T_TUS_DESCRIPCION) VALUES (?,?)"
        elif argument == "TIPOS_DNI": return "INSERT INTO TIPOS_DNI (T_DNI_ACTIVO,T_DNI_DESCRIPCION) VALUES (?,?)"
        elif argument == "ETAPAS": return "INSERT INTO ETAPAS (T_ETA_ACTIVA, T_ETA_DESCRIPCION) VALUES (?,?)"
        elif argument == "TIPO_ACCIONES": return "INSERT INTO TIPO_ACCIONES (T_TAC_ACTIVO,T_TAC_DESCRIPCION) VALUES (?,?)"
        elif argument == "CATEGORIAS": return "INSERT INTO CATEGORIAS (T_CAT_ACTIVA, T_CAT_NOMBRE, T_CAT_ORDEN) VALUES (?,?,?)"
        elif argument == "COMBOS": return "INSERT INTO COMBOS (T_COMB_FECH_INI, T_COMB_FECH_FIN, T_COMB_PRECIO, T_COMB_NOMBRE, T_COMB_DETALLE,T_COMB_ACTIVO,T_COMB_PORC_RESERVA,T_COMB_FECHA_HORA_RESERVA) VALUES (?,?,?,?,?,?,?,?)"
        pass      
        

    def update_case(self, argument):
        if argument == "PRODUCTOS": return "UPDATE PRODUCTOS SET T_PROD_FECH_INI = ? ,T_PROD_FECH_FIN = ? ,T_PROD_NOMBRE = ?,T_PROD_DETALLE = ?,T_PROD_ACTIVO = ?,T_NIV_ID1 = ?,T_PROD_PRECIO = ?,T_PROD_PORC_RESERVA = ?, T_PROD_FECHA_HORA_RESERVA = ?, T_PROD_ORDEN= ? WHERE T_PROD_ID = ?"
        pass      
       

    def selectId_case(self, argument):
        if argument == "PRODUCTOS": return "SELECT * FROM PRODUCTOS WHERE T_PROD_ID = ?"
        pass      

    def max_case(self, argument):
        if argument == "PRODUCTOS": return "SELECT MAX(T_PROD_ID) FROM PRODUCTOS"
        pass      

    def delete_case(self, argument):
        if argument == "PRODUCTOS": return "DELETE FROM PRODUCTOS WHERE T_PROD_ID = ?"
        pass      
 
#====================CONSULTAS====================
    def insert(self, parameter_list, tabla):
        if self.conexion.is_connected():
            try:
                cur = self.con.cursor()
                cur.execute(self.insert_case(tabla), parameter_list)
                self.con.commit()    
            except:
                print("No se pudo concectar a la base de datos")
        pass     
    
    def update(self, parameter_list, tabla):
        if self.conexion.is_connected():
            try:
                cur = self.con.cursor()
                cur.execute(self.update_case(tabla), parameter_list)
                self.con.commit()      
            except:
                print("No se pudo concectar a la base de datos") 
        pass    

    def delete(self, id, tabla):
        if self.conexion.is_connected():
            try:
                cur = self.con.cursor()
                cur.execute(self.delete_case(tabla), [id])
                self.con.commit()   
            except:
                print("No se pudo concectar a la base de datos")  
        pass       

    def selectId(self, id, tabla):
        if self.conexion.is_connected():
            try:
                cursor = self.con.execute(self.insert_case(tabla), [id])
                return cursor.fetchall()   
            except:
                print("No se pudo concectar a la base de datos")
        pass    

    def selectAll(self, tabla, condiciones = None):
        if self.conexion.is_connected():
            try:
                if condiciones == None :
                    cursor = self.con.execute("SELECT * FROM " + tabla)
                    return cursor.fetchall()
                else :
                    consulta = "SELECT * FROM " + tabla
                    consulta += " WHERE 1 = 1 "
                    for i in range(len(condiciones)):
                        if i%2 == 0:
                            consulta += "and " + str(condiciones[i])
                        else :
                            consulta += " = " + str(condiciones[i])
                    cursor = self.con.execute(consulta)
                    return cursor.fetchall()
            except:
                print("No se pudo concectar a la base de datos")
        pass    
    
    def selectMax(self, tabla):
        if self.conexion.is_connected():
            try:        
                cur = self.con.cursor()
                cur.execute(self.max_case(tabla))
                return cur.fetchone()[0]
            except:
                print("No se pudo concectar a la base de datos")
        pass    


