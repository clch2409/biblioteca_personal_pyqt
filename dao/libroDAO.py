from db import DataBase
from pymysql.err import IntegrityError, MySQLError
from model.libro import Libro

class LibroDAO:

  def __init__(self, db):
    self.db: DataBase = db

  def listarLibros(self):
    conn = None
    try:
      conn = self.db.conectar()
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM libro")
      return [Libro(l[0], l[1], l[2], l[3]) for l in cursor.fetchall()]
    except MySQLError as e:
      print(e)
      return []
    finally:
      if conn is not None:
        conn.close()

  def crearLibro(self, titulo_libro, id_genero, id_autor):
    conn = None
    try:
      conn = self.db.conectar()
      cursor = conn.cursor()
      cursor.execute(
        "INSERT INTO libro (titulo_libro, id_genero, id_autor) "
        "VALUES (%s, %s, %s)",
        (titulo_libro, id_genero, id_autor)
      )
      libro_creado = Libro(cursor.lastrowid, titulo_libro, id_genero, id_autor)
      conn.commit()
      return libro_creado
    except IntegrityError as e:
      if conn is not None:
        conn.rollback()
      print(e)
      return None
    except MySQLError as e:
      if conn is not None:
        conn.rollback()
      print(e)
      return None
    finally:
      if conn is not None:
        conn.close()

