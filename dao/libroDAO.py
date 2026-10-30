from db import DataBase
from pyodbc import IntegrityError
from model.libro import Libro

class LibroDAO:

  def __init__(self, db):
    self.db: DataBase = db

  def listarLibros(self):
    conn = self.db.conectar()
    cursor = conn.cursor()

    try:
      cursor.execute("SELECT * FROM libro")
    except IntegrityError as e:
      print(e)

    libros = [Libro(l[0], l[1], l[2], l[3]) for l in cursor.fetchall()]

    conn.commit()
    conn.close()
    return libros

  def crearLibro(self, titulo_libro, id_genero, id_autor):
    conn = self.db.conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO libro (titulo_libro, id_genero, id_autor) OUTPUT INSERTED.* VALUES (?, ?, ?)", (titulo_libro, id_genero, id_autor))

    libro = cursor.fetchone()
    libro_creado = Libro(libro[0], libro[1], libro[2], libro[3])

    conn.commit()
    conn.close()

    return libro_creado;



    


