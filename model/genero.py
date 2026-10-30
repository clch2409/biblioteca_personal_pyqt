class Genero:

  def __init__(self, id_genero=None, nombre_genero=None):
    self.id_genero = id_genero
    self.nombre_genero = nombre_genero

  def __str__(self):
    return f"Genero(id={self.id_genero}, nombre='{self.nombre_genero}')"
