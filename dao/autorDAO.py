from db import DataBase
from pymysql.err import MySQLError
from model.autor import Autor


class AutorDAO:

  def __init__(self, db):
    self.db: DataBase = db

  def listarAutores(self):
    conn = None
    try:
      conn = self.db.conectar()
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM autor")
      return [Autor(a[0], a[1], a[2]) for a in cursor.fetchall()]
    except MySQLError as e:
      print(e)
      return []
    finally:
      if conn is not None:
        conn.close()
