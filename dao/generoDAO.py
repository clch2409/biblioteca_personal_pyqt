from db import DataBase
from pyodbc import IntegrityError
from model.genero import Genero


class GeneroDAO:

  def __init__(self, db):
    self.db: DataBase = db

  def listarGeneros(self):
    conn = self.db.conectar()
    cursor = conn.cursor()

    try:
      cursor.execute("SELECT * FROM genero")
    except IntegrityError as e:
      print(e)

    generos = [Genero(g[0], g[1]) for g in cursor.fetchall()]

    conn.commit()
    conn.close()
    return generos
