from db import DataBase
from pyodbc import IntegrityError
from model.autor import Autor


class AutorDAO:

  def __init__(self, db):
    self.db: DataBase = db

  def listarAutores(self):
    conn = self.db.conectar()
    cursor = conn.cursor()

    try:
      cursor.execute("SELECT * FROM autor")
    except IntegrityError as e:
      print(e)

    autores = [Autor(a[0], a[1], a[2]) for a in cursor.fetchall()]

    
    conn.commit()
    conn.close()
    return autores
