from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6 import uic
from db import DataBase
from dao.usuarioDAO import UsuarioDAO


class DialogRegistro(QDialog):
  def __init__(self):
    super().__init__()
    uic.loadUi("vtnRegistro.ui", self)

    self.db = DataBase()
    self.usuariodao = UsuarioDAO(self.db)
    self.usuario_registrado = ""
    self.btnEnviar.clicked.connect(self.validarRegistro)
    self.btnRegresar.clicked.connect(self.regresarLogin)
    self.setTabOrder(self.txtUsuario, self.txtContra)
    self.setTabOrder(self.txtContra, self.txtRepetir)
    self.setTabOrder(self.txtRepetir, self.btnEnviar)

  def validarRegistro(self):
    nombre_usuario = str(self.txtUsuario.text()).strip()
    contrasena = str(self.txtContra.text()).strip()
    repetir = str(self.txtRepetir.text()).strip()
    if (len(nombre_usuario) == 0 or len(contrasena) == 0 or len(repetir) == 0):
      QMessageBox.warning(self, "Campos Obligatorios", "Todos los campos son obligatorios")
      return  

    nombre_usuario_existe = self.usuariodao.validarExistenciaUsuario(nombre_usuario)
    if nombre_usuario_existe:
      QMessageBox.warning(self, "Nombre de usuario Existente", "El nombre de usuario ya existe, elija otro")
      return

    if (contrasena != repetir):
      QMessageBox.warning(self, "Contraseñas Diferentes", "Las contraseñas ingresadas no coinciden")
      return

    if self.usuariodao.crearUsuario(nombre_usuario, contrasena):
      QMessageBox.information(self, "Usuario Creado Correctamente", "El usuario se ha creado correctamente, pasará a la ventana de Login")
      self.usuario_registrado = nombre_usuario
      self.accept()
    else:
      QMessageBox.warning(self, "Error", "Hubo un error al crear el usuario")

  def regresarLogin(self):
    self.reject()


    