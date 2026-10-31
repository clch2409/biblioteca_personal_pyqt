import pymysql
import os
from dotenv import load_dotenv


class DataBase:

  def __init__(self):
    load_dotenv()
    self.servername = "localhost"
    self.database = "biblioteca_personal"
    self.username = "root"
    self.password = os.getenv("DB_PASSWORD")

  def conectar(self):
    return pymysql.connect(
      host=self.servername,
      user=self.username,
      password=self.password,
      port=3306,
      database=self.database,
      charset='utf8mb4'
    )

  def crear_tablas(self):
    conn = self.conectar()
    cursor = conn.cursor()

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS autor(
        id_autor INT PRIMARY KEY AUTO_INCREMENT,
        nombre_autor VARCHAR(30) NOT NULL,
        fecha_nacimiento DATE
      )
    """)

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS genero(
        id_genero INT PRIMARY KEY AUTO_INCREMENT,
        nombre_genero VARCHAR(20) NOT NULL
      )
    """)

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS libro(
        id_libro INT PRIMARY KEY AUTO_INCREMENT,
        titulo_libro VARCHAR(30) NOT NULL,
        id_genero INT NOT NULL,
        id_autor INT NOT NULL,
        CONSTRAINT FK_ID_GENERO FOREIGN KEY (id_genero)
          REFERENCES genero(id_genero),
        CONSTRAINT FK_ID_AUTOR FOREIGN KEY (id_autor)
          REFERENCES autor(id_autor)
      )
    """)

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS estado_lectura(
        id_estado_lectura INT PRIMARY KEY AUTO_INCREMENT,
        nombre_estado VARCHAR(30) NOT NULL
      )
    """)

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS lectura(
        id_lectura INT PRIMARY KEY AUTO_INCREMENT,
        id_libro INT NOT NULL,
        cant_paginas_leidas INT NOT NULL,
        id_estado_lectura INT NOT NULL,
        CONSTRAINT FK_ID_LIBRO FOREIGN KEY (id_libro)
          REFERENCES libro(id_libro),
        CONSTRAINT FK_ID_ESTADO_LECTURA FOREIGN KEY (id_estado_lectura)
          REFERENCES estado_lectura(id_estado_lectura)
      )
    """)

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS usuario(
        id_usuario INT PRIMARY KEY AUTO_INCREMENT,
        nombre_usuario VARCHAR(30) NOT NULL,
        contrasena VARCHAR(255) NOT NULL,
        rol VARCHAR(10) NOT NULL DEFAULT 'admin'
      )
    """)

    conn.commit()
    conn.close()

