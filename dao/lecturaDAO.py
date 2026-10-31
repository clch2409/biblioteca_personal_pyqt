from db import DataBase
from pymysql.err import IntegrityError, MySQLError
from model.historial import Historial

class LecturaDAO:
  def __init__(self, db):
    self.db : DataBase = db

  def crearNuevaLectura(self, id_libro, id_estado_lectura, cant_paginas):
    conn = None
    try:
      conn = self.db.conectar()
      cursor = conn.cursor()
      cursor.execute(
        "INSERT INTO lectura (id_libro, cant_paginas_leidas, id_estado_lectura) "
        "VALUES (%s, %s, %s)",
        (id_libro, cant_paginas, id_estado_lectura)
      )
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

  def obtenerHistorialLecturas(self):
    conn = None
    try:
      conn = self.db.conectar()
      cursor = conn.cursor()
      cursor.execute("""
      SELECT l.titulo_libro, a.nombre_autor, g.nombre_genero, le.cant_paginas_leidas , e.nombre_estado
      FROM lectura le
      JOIN estado_lectura e ON le.id_estado_lectura = e.id_estado_lectura
      JOIN libro l ON l.id_libro = le.id_libro
      JOIN genero g ON g.id_genero = l.id_genero
      JOIN autor a ON a.id_autor = l.id_autor
    """)
      return [Historial(h[0], h[1], h[2], h[3], h[4]) for h in cursor.fetchall()]
    except MySQLError as e:
      print(e)
      return []
    finally:
      if conn is not None:
        conn.close()

  