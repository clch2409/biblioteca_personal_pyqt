
class Lectura:

  def __init__(self, id_lectura, id_libro, id_estado_lectura, cant_paginas_leidas):
    self.id_lectura = id_lectura
    self.id_libro = id_libro
    self.id_estado_lectura = id_estado_lectura
    self.cant_paginas_leidas = cant_paginas_leidas

  def __str__(self):
    return (
      f"Lectura(id={self.id_lectura}, id_libro={self.id_libro}, "
      f"paginas_leidas={self.cant_paginas_leidas}, "
      f"id_estado_lectura={self.id_estado_lectura})"
    )