-- Active: 1665440290776@@127.0.0.1@3306@easytravel
CREATE DATABASE EASYTRAVEL;

USE EASYTRAVEL;

CREATE TABLE TIPOS_DNI (
    T_DNI_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   
    T_DNI_ACTIVO BOOLEAN,
    T_DNI_DESCRIPCION VARCHAR (30)
);

CREATE TABLE TIPOS_USUARIOS (
    T_TUS_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   
    T_TUS_ACTIVO BOOLEAN,
    T_TUS_DESCRIPCION VARCHAR (30)
);

CREATE TABLE USUARIOS (
    T_USU_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    T_USU_NOMBRES VARCHAR (30),
    T_USU_APELLIDOS VARCHAR (30),
    T_USU_FECH_NAC DATE,
    T_USU_DNI VARCHAR (20),
    T_DNI_ID1 INT, 
    T_USU_PASSW VARCHAR (100),
    T_USU_NPERFIL VARCHAR (30),
    T_TUS_ID1 INT,
    T_USU_ACTIVO BOOLEAN,
    T_USU_EMAIL VARCHAR (50),
    T_USU_CELULAR VARCHAR (25),
    T_USU_PUNTAJE INT,
    FOREIGN KEY (T_DNI_ID1) REFERENCES TIPOS_DNI(T_DNI_ID),
    FOREIGN KEY (T_TUS_ID1) REFERENCES TIPOS_USUARIOS(T_TUS_ID)
);

CREATE TABLE ETAPAS (
    T_ETA_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   
    T_ETA_ACTIVA BOOLEAN,
    T_ETA_DESCRIPCION VARCHAR (30)
);

CREATE TABLE TIPO_ACCIONES (
    T_TAC_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   
    T_TAC_ACTIVO BOOLEAN,
    T_TAC_DESCRIPCION VARCHAR (30)
);

CREATE TABLE COMBOS (
    T_COMB_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,    
    T_COMB_FECH_INI DATETIME,
    T_COMB_FECH_FIN DATETIME,
    T_COMB_PRECIO FLOAT,
    T_COMB_NOMBRE VARCHAR (30),
    T_COMB_DETALLE VARCHAR (500),
    T_COMB_ACTIVO BOOLEAN,
    T_COMB_PORC_RESERVA INT,
    T_COMB_FECHA_HORA_RESERVA DATETIME --CUANDO CADUCA LA RESERVA
);

CREATE TABLE NIVELES_PRODUCTOS (
    T_NIV_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   
    T_NIV_ACTIVO BOOLEAN,
    T_NIV_DESCRIPCION VARCHAR (30)
);

CREATE TABLE PRODUCTOS (
    T_PROD_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,    
    T_PROD_FECH_INI DATE,
    T_PROD_FECH_FIN DATE,
    T_PROD_NOMBRE VARCHAR (30),
    T_PROD_DETALLE VARCHAR (500),
    T_PROD_ACTIVO BOOLEAN,
    T_NIV_ID1 INT, 
    T_PROD_PRECIO FLOAT,
    T_PROD_PORC_RESERVA INT,
    T_PROD_FECHA_HORA_RESERVA DATETIME, --CUANDO CADUCA LA RESERVA
    T_PROD_ORDEN INT,
    FOREIGN KEY (T_NIV_ID1) REFERENCES NIVELES_PRODUCTOS(T_NIV_ID)
);

CREATE TABLE ACCIONES (
    T_ACC_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    T_ACC_FECH_HORA DATETIME,
    T_ACC_COMBO_PROD BOOLEAN,
    T_USU_ID1 INT, 
    T_TAC_ID1 INT, 
    T_ETA_ID1 INT, 
    T_COMB_ID3 INT, 
    T_PROD_ID3 INT, 
    FOREIGN KEY (T_USU_ID1) REFERENCES USUARIOS(T_USU_ID),
    FOREIGN KEY (T_TAC_ID1) REFERENCES TIPO_ACCIONES(T_TAC_ID),
    FOREIGN KEY (T_ETA_ID1) REFERENCES ETAPAS(T_ETA_ID),
    FOREIGN KEY (T_COMB_ID3) REFERENCES COMBOS(T_COMB_ID),
    FOREIGN KEY (T_PROD_ID3) REFERENCES PRODUCTOS(T_PROD_ID)
);

CREATE TABLE CATEGORIAS (
    T_CAT_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   
    T_CAT_ACTIVA BOOLEAN,
    T_CAT_NOMBRE VARCHAR (30),
    T_CAT_ORDEN INT
);

CREATE TABLE SUBCATEGORIAS (
    T_SUB_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   
    T_SUB_ACTIVA BOOLEAN,
    T_SUB_NOMBRE VARCHAR (30),
    T_SUB_ORDEN INT
);

CREATE TABLE PUBLICIDADES (
    T_PUB_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   
    T_PUB_ACTIVA BOOLEAN,
    T_PUB_FECH_INI DATE,
    T_PUB_FECH_FIN DATE,
    T_PUB_DETALLE VARCHAR (100)
);

CREATE TABLE EMPRESAS (
    T_EMP_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   
    T_PUB_ID1 INT,
    T_EMP_ACTIVA BOOLEAN,
    T_EMP_NOMBRE VARCHAR (30),
    T_EMP_LOGO BLOB,
    T_EMP_DESCRIPCION VARCHAR (100),
    T_EMP_ES_ASOCIADA BOOLEAN,
    FOREIGN KEY (T_PUB_ID1) REFERENCES PUBLICIDADES(T_PUB_ID)
);

CREATE TABLE IMAGENES (
    T_IMG_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  
    T_IMG_IMAGEN BLOB
);

CREATE TABLE TIPOS_SERVICIOS (
    T_TSERV_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   
    T_TSERV_ACTIVO BOOLEAN,
    T_TSERV_NOMBRE VARCHAR (30)
);

CREATE TABLE SERVICIOS (
    T_SERV_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   
    T_TSERV_ID1 INT,
    T_SERV_ACTIVO BOOLEAN,
    T_SERV_NOMBRE VARCHAR (30),
    T_SERV_DESCRIPCION VARCHAR (100),
    FOREIGN KEY (T_TSERV_ID1) REFERENCES TIPOS_SERVICIOS(T_TSERV_ID)
);

CREATE TABLE COMB_NIV (
    T_COMB_ID1 INT,
    T_NIV_ID2 INT,
    T_C_N_ACTIVO BOOLEAN,
    FOREIGN KEY (T_NIV_ID2) REFERENCES NIVELES_PRODUCTOS(T_NIV_ID),
    FOREIGN KEY (T_COMB_ID1) REFERENCES COMBOS(T_COMB_ID),
    CONSTRAINT PK_COMB_NIV PRIMARY KEY (T_COMB_ID1, T_NIV_ID2)
);

CREATE TABLE COMB_PROD (
    T_COMB_ID2 INT, 
    T_PROD_ID2 INT, 
    CONSTRAINT PK_COMB_NIV PRIMARY KEY (T_COMB_ID2, T_PROD_ID2),
    FOREIGN KEY (T_COMB_ID2) REFERENCES COMBOS(T_COMB_ID),
    FOREIGN KEY (T_PROD_ID2) REFERENCES PRODUCTOS(T_PROD_ID)
);

CREATE TABLE CAT_SUB (
    T_C_S_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   
    T_CAT_ID1 INT, 
    T_SUB_ID1 INT, 
    T_C_S_ACTIVO BOOLEAN,
    FOREIGN KEY (T_CAT_ID1) REFERENCES CATEGORIAS(T_CAT_ID),
    FOREIGN KEY (T_SUB_ID1) REFERENCES SUBCATEGORIAS(T_SUB_ID)
);

CREATE TABLE CAT_SUB_PROD ( 
    T_PROD_ID1 INT, 
    T_C_S_ID1 INT, 
    T_C_S_P_ACTIVO BOOLEAN,
    CONSTRAINT T_C_S_P_ID PRIMARY KEY (T_C_S_ID1, T_PROD_ID1),
    FOREIGN KEY (T_PROD_ID1) REFERENCES PRODUCTOS(T_PROD_ID),
    FOREIGN KEY (T_C_S_ID1) REFERENCES CAT_SUB(T_C_S_ID)
);

CREATE TABLE EMP_SERV (
    T_E_S_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   
    T_SERV_ID1 INT, 
    T_EMP_ID1 INT, 
    T_E_S_ACTIVO BOOLEAN,
    FOREIGN KEY (T_SERV_ID1) REFERENCES SERVICIOS(T_SERV_ID),
    FOREIGN KEY (T_EMP_ID1) REFERENCES EMPRESAS(T_EMP_ID)
);

CREATE TABLE PUB_IMG (
    T_P_I_ACTIVA BOOLEAN,
    CONSTRAINT T_C_S_P_ID PRIMARY KEY (T_PUB_ID2, T_IMG_ID1),
    T_PUB_ID2 INT,
    FOREIGN KEY (T_PUB_ID2) REFERENCES PUBLICIDADES(T_PUB_ID),
    T_IMG_ID1 INT,
    FOREIGN KEY (T_IMG_ID1) REFERENCES IMAGENES(T_IMG_ID)
);

CREATE TABLE EMP_SERV_PROD (
    T_PROD_ID4 INT,
    T_E_S_ID1 INT,
    T_E_S_P_ACTIVO BOOLEAN,
    CONSTRAINT T_E_S_P_ID PRIMARY KEY (T_E_S_ID1, T_PROD_ID4),
    FOREIGN KEY (T_PROD_ID4) REFERENCES PRODUCTOS(T_PROD_ID),
    FOREIGN KEY (T_E_S_ID1) REFERENCES EMP_SERV(T_E_S_ID)
);