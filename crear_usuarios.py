from db import DataBase
from dao.usuarioDAO import UsuarioDAO

if __name__ == "__main__":
  base = DataBase()
  dao = UsuarioDAO(base)
  # usuario1 = dao.crearUsuario("clch", "admin123")
  # print(usuario1)
  
  usuarioLogin = dao.validarLogin("clch2409", "admin")
  print(usuarioLogin)