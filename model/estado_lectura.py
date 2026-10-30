class EstadoLectura:

  def __init__(self, id_estado_lectura=None, nombre_estado=None):
    self.id_estado_lectura = id_estado_lectura
    self.nombre_estado = nombre_estado

  def __str__(self):
    return (
      f"EstadoLectura(id={self.id_estado_lectura}, "
      f"nombre='{self.nombre_estado}')"
    )
