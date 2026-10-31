from db import DataBase
from pymysql.err import MySQLError
from model.estado_lectura import EstadoLectura


class EstadoLecturaDAO:

  def __init__(self, db):
    self.db: DataBase = db

  def listarEstadosLectura(self):
    conn = None
    try:
      conn = self.db.conectar()
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM estado_lectura")
      return [EstadoLectura(e[0], e[1]) for e in cursor.fetchall()]
    except MySQLError as e:
      print(e)
      return []
    finally:
      if conn is not None:
        conn.close()
