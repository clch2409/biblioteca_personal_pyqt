from db import DataBase
from pymysql.err import MySQLError
from model.genero import Genero


class GeneroDAO:

  def __init__(self, db):
    self.db: DataBase = db

  def listarGeneros(self):
    conn = None
    try:
      conn = self.db.conectar()
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM genero")
      return [Genero(g[0], g[1]) for g in cursor.fetchall()]
    except MySQLError as e:
      print(e)
      return []
    finally:
      if conn is not None:
        conn.close()
