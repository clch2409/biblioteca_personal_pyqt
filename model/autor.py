class Autor:

  def __init__(self, id_autor=None, nombre_autor=None, fecha_nacimiento=None):
    self.id_autor = id_autor
    self.nombre_autor = nombre_autor
    self.fecha_nacimiento = fecha_nacimiento

  def __str__(self):
    return (
      f"Autor(id={self.id_autor}, nombre='{self.nombre_autor}', "
      f"fecha_nacimiento={self.fecha_nacimiento})"
    )
