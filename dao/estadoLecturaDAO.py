from db import DataBase
from pyodbc import IntegrityError
from model.estado_lectura import EstadoLectura


class EstadoLecturaDAO:

  def __init__(self, db):
    self.db: DataBase = db

  def listarEstadosLectura(self):
    conn = self.db.conectar()
    cursor = conn.cursor()

    try:
      cursor.execute("SELECT * FROM estado_lectura")
    except IntegrityError as e:
      print(e)

    estados = [EstadoLectura(e[0], e[1]) for e in cursor.fetchall()]

    conn.commit()
    conn.close()
    return estados
