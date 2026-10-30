

class Libro:

  def __init__(self, id_libro=None, titulo_libro=None, id_genero=None, id_autor=None):
    self.id_libro = id_libro
    self.titulo_libro = titulo_libro
    self.id_genero = id_genero
    self.id_autor = id_autor

  def __str__(self):
    return (
      f"Libro(id={self.id_libro}, titulo='{self.titulo_libro}', "
      f"id_genero={self.id_genero}, id_autor={self.id_autor})"
    )
