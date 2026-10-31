from db import DataBase
from model.usuario import Usuario
from pymysql.err import IntegrityError, MySQLError
import bcrypt


class UsuarioDAO:

  def __init__(self, bd):
    self.bd: DataBase = bd


  def crearUsuario(self, nombre, contra: str):
    conn = None
    try:
      conn = self.bd.conectar()
      cursor = conn.cursor()
      contrasena_ingresada_bytes = contra.encode('utf-8')
      salt = bcrypt.gensalt()
      contrasena_hash = bcrypt.hashpw(
        contrasena_ingresada_bytes, salt
      ).decode('utf-8')
      cursor.execute("""
            INSERT INTO usuario (nombre_usuario, contrasena)
            VALUES (%s, %s)
          """, (nombre, contrasena_hash))
      conn.commit()
      return True
    except IntegrityError as e:
      if conn is not None:
        conn.rollback()
      print(e)
      return False
    except MySQLError as e:
      if conn is not None:
        conn.rollback()
      print(e)
      return False
    finally:
      if conn is not None:
        conn.close()

  def validarLogin(self, nombre, contra: str):
    conn = None
    try:
      conn = self.bd.conectar()
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM usuario WHERE nombre_usuario = %s", (nombre,))

      usuario_array = cursor.fetchone()

      if (usuario_array):
        usuario_encontrado = Usuario(
          usuario_array[0], usuario_array[1], usuario_array[2], usuario_array[3]
        )
        contrasena_usuario = usuario_encontrado.contrasena.encode('utf-8')
        contrasena_ingresada = contra.encode('utf-8')

        if (bcrypt.checkpw(contrasena_ingresada, contrasena_usuario)):
          return usuario_encontrado
      return 0
    except MySQLError as e:
      print(e)
      return 0
    finally:
      if conn is not None:
        conn.close()
    