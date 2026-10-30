class Usuario:

	def __init__(self, id_usuario=None, nombre_usuario=None, contrasena=None, rol=None):
		self.id_usuario = id_usuario
		self.nombre_usuario = nombre_usuario
		self.contrasena = contrasena
		self.rol = rol

	def __str__(self):
		return (
			f"Usuario(id={self.id_usuario}, nombre='{self.nombre_usuario}', "
			f"contrasena='{self.contrasena}', rol='{self.rol}')"
		)

