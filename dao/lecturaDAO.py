from db import DataBase
from PyQt6.QtWidgets import QMessageBox
from pyodbc import IntegrityError
from model.historial import Historial

class LecturaDAO:
  def __init__(self, db):
    self.db : DataBase = db

  def crearNuevaLectura(self, id_libro, id_estado_lectura, cant_paginas):
    conn = self.db.conectar()
    cursor = conn.cursor()
    registrado = False
    try:
      cursor.execute("INSERT INTO lectura (id_libro, cant_paginas_leidas, id_estado_lectura) VALUES (?, ?, ?)", (id_libro, cant_paginas, id_estado_lectura))
    except IntegrityError as e:
      print(e)
    else:
      registrado = True

    conn.commit()
    conn.close()
    return registrado

  def obtenerHistorialLecturas(self):
    conn = self.db.conectar()
    cursor = conn.cursor()
    historial = []
    try:
      cursor.execute("""
      SELECT l.titulo_libro, a.nombre_autor, g.nombre_genero, le.cant_paginas_leidas , e.nombre_estado
      FROM lectura le
      JOIN estado_lectura e ON le.id_estado_lectura = e.id_estado_lectura
      JOIN libro l ON l.id_libro = le.id_libro
      JOIN genero g ON g.id_genero = l.id_genero
      JOIN autor a ON a.id_autor = l.id_autor
    """)
      historial = [Historial(h[0], h[1], h[2], h[3], h[4]) for h in cursor.fetchall()]
    except Exception as e:
      print(e)

    conn.commit()
    conn.close()
    return historial

  