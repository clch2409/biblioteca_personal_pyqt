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
    self.btnEnviar.clicked.connect(self.validarRegistro)

  def validarRegistro(self):
    nombre_usuario = self.txtUsuario.text()
    nombre_usuario_existe = self.usuariodao.validarExistenciaUsuario(nombre_usuario)
    if nombre_usuario_existe:
      QMessageBox.warning("El nombre de usuario ya existe, elija otro", "Nombre de usuario Existente")
      