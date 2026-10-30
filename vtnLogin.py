# En login.py
from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6 import uic
from dao.usuarioDAO import UsuarioDAO
from db import DataBase

class DialogLogin(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("vtnLogin.ui", self)
        
        self.db = DataBase()
        self.usuarioDao = UsuarioDAO(self.db)
        self.btnInicioSesion.clicked.connect(self.validarLogin)

    def validarLogin(self):
        nombre = self.txtUsuario.text()
        contra = self.txtContra.text()
        usuario = self.usuarioDao.validarLogin(nombre, contra)
        
        if usuario:
            QMessageBox.information(self, "Ingreso correcto", f"Bienvenido {usuario.nombre_usuario}")
            self.accept() # Esto le dice a PyQt que el diálogo se cerró con éxito (True)
        else:
            QMessageBox.warning(self, "Credenciales Incorrectas", "Su usuario o contraseña son incorrectos")