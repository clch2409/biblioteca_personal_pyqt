from getpass import getpass
from db import DataBase
from dao.usuarioDAO import UsuarioDAO

if __name__ == "__main__":
  dao = UsuarioDAO(DataBase())
  nombre = input("Usuario: ")
  contra = getpass("Contraseña: ")
  print("Usuario creado" if dao.crearUsuario(nombre, contra) else "No se pudo crear")