import pyodbc


class DataBase:

  def __init__(self):
    self.servername = r"LAPTOP-CVKI77EA\CLCH2409"
    self.database = "biblioteca_personal"

    self.connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={self.servername};DATABASE={self.database};Trusted_Connection=yes;TrustServerCertificate=yes;'


  def conectar(self):
    return pyodbc.connect(self.connection_string)

  def crear_tablas(self):
    conn = self.conectar()
    cursor = conn.cursor()

    cursor.execute("""
      CREATE TABLE autor(
        id_autor INT PRIMARY KEY IDENTITY(1,1),
        nombre_autor VARCHAR(30) NOT NULL,
        fecha_nacimiento DATE
      )
    """)

    cursor.execute("""
      CREATE TABLE genero(
        id_genero INT PRIMARY KEY IDENTITY(1,1),
        nombre_genero VARCHAR(20) NOT NULL
      )
    """)

    cursor.execute("""
      CREATE TABLE libro(
        id_libro INT PRIMARY KEY IDENTITY(1,1),
        titulo_libro VARCHAR(30) NOT NULL,
        id_genero INT NOT NULL,
        id_autor INT NOT NULL
    )
    """)

    cursor.execute("""
      CREATE TABLE estado_lectura(
        id_estado_lectura INT PRIMARY KEY IDENTITY(1,1),
        nombre_estado VARCHAR(30) NOT NULL
      )
    """)

    cursor.execute("""
      CREATE TABLE lectura(
        id_lectura INT PRIMARY KEY IDENTITY(1,1),
        id_libro INT NOT NULL,
        cant_paginas_leidas INT NOT NULL,
        id_estado_lectura INT NOT NULL
      )
    """)

    cursor.execute("""
      CREATE TABLE usuario(
        id_usuario INT PRIMARY KEY IDENTITY(1,1),
        nombre_usuario VARCHAR(30) NOT NULL,
        contrasena VARCHAR(30) NOT NULL,
        rol VARCHAR(10) NOT NULL
      )
    """)

    conn.commit()
    conn.close()


