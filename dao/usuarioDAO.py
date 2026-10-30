from db import DataBase
from model.usuario import Usuario
import bcrypt


class UsuarioDAO:

  def __init__(self, bd):
    self.bd: DataBase = bd


  def crearUsuario(self, nombre, contra: str):
    conn = self.bd.conectar()
    cursor = conn.cursor()
    usuario_creado = ""

    contrasena_ingresada_bytes = contra.encode('utf-8')
    salt = bcrypt.gensalt()
    contrasena_hash = bcrypt.hashpw(contrasena_ingresada_bytes, salt).decode('utf-8')

    try:
      cursor.execute("""
            INSERT INTO usuario (nombre_usuario, contrasena)
            OUTPUT INSERTED.*
            VALUES (?, ?)
          """, (nombre, contrasena_hash))
      usuario_array = cursor.fetchone()
      usuario_creado = Usuario(usuario_array[0], usuario_array[1], usuario_array[2], usuario_array[3])
      conn.commit()
    except Exception as e:
      print(e)
    finally:
      conn.close()

    
    return usuario_creado

  def validarLogin(self, nombre, contra: str):
    conn = self.bd.conectar()
    cursor = conn.cursor()
    respuesta = 0

    try:
      cursor.execute("SELECT * FROM usuario WHERE nombre_usuario = ?", (nombre,))

      usuario_array = cursor.fetchone()

      if (usuario_array):
        usuario_encontrado= Usuario(usuario_array[0], usuario_array[1], usuario_array[2], usuario_array[3])
        contrasena_usuario = usuario_encontrado.contrasena.encode('utf-8')
        contrasena_ingresada = contra.encode('utf-8')

        if (bcrypt.checkpw(contrasena_ingresada, contrasena_usuario)):
          respuesta = usuario_encontrado

      conn.commit()
    except InterruptedError as i:
      print(i)
    except Exception as e:
      print(e)
    finally:
      conn.close()

    return respuesta
    