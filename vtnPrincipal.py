import sys
from PyQt6.QtWidgets import QApplication,QMainWindow, QTableWidgetItem, QDialog, QMessageBox, QHeaderView
from PyQt6 import uic
from dao.autorDAO import AutorDAO
from dao.estadoLecturaDAO import EstadoLecturaDAO
from dao.generoDAO import GeneroDAO
from dao.libroDAO import LibroDAO
from dao.lecturaDAO import LecturaDAO
from db import DataBase
from vtnLogin import DialogLogin
from vtnRegistro import DialogRegistro


class vtnPrincipal(QMainWindow):

  def __init__(self):
    super().__init__()
    uic.loadUi('vtnPrincipal.ui', self)
    self.setWindowTitle("Registro de Lecturas")
    self.db = DataBase()
    self.autorDao = AutorDAO(self.db)
    self.estadoLecturaDao = EstadoLecturaDAO(self.db)
    self.generoDao = GeneroDAO(self.db)
    self.libroDao = LibroDAO(self.db)
    self.lecturaDao = LecturaDAO(self.db)
    self.llenarCombosHistorial()
    self.btnEnviar.clicked.connect(self.obtenerDatosHistorial)
    self.actualizarTablaHistorial()
    self.actualizarTablaGeneros()
    self.stackedWidget.setCurrentIndex(0)
    self.btnLectura.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
    self.btnAutor.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
    self.btnGenero.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
    self.tblLectura.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    self.tblGenero.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

  def llenarCombosHistorial(self):
    nombresAutores = [(a.id_autor, a.nombre_autor) for a in self.autorDao.listarAutores()]
    nombresEstadosLecturas = [(e.id_estado_lectura, e.nombre_estado) for e in self.estadoLecturaDao.listarEstadosLectura()]
    nombresGeneros = [(g.id_genero, g.nombre_genero) for g in self.generoDao.listarGeneros()]

    for id, autor in nombresAutores:
      self.cmbAutor.addItem(autor, id)

    for id, estado in nombresEstadosLecturas:
      self.cmbEstadoLectura.addItem(estado, id)

    for id, genero in nombresGeneros:
      self.cmbGenero.addItem(genero, id)

  def obtenerDatosHistorial(self):
    titulo = self.txtTitulo.text().strip()
    if not titulo:
      QMessageBox.warning(self, "Datos incompletos", "Ingresa el título del libro")
      return

    autor = self.cmbAutor.currentData()
    genero = self.cmbGenero.currentData()
    pags = self.spnPagsLeidas.value()
    estado = self.cmbEstadoLectura.currentData()

    libro_creado = self.libroDao.crearLibro(titulo, genero, autor)
    if libro_creado is None:
      QMessageBox.critical(self, "Error", "No se pudo guardar el libro")
      return

    if not self.lecturaDao.crearNuevaLectura(libro_creado.id_libro, estado, pags):
      QMessageBox.critical(self, "Error", "No se pudo guardar la lectura")
      return

    self.actualizarTabla()

  def actualizarTablaHistorial(self):
    historial = self.lecturaDao.obtenerHistorialLecturas()

    self.tblLectura.setColumnCount(5)
    self.tblLectura.setHorizontalHeaderLabels(["Titulo", "Autor", "Género", "Páginas", "Estado"])
    self.tblLectura.setRowCount(len(historial))

    for index_fila, historial_obj in enumerate(historial):
      dato_list = [
        historial_obj.titulo,
        historial_obj.autor,
        historial_obj.genero, 
        historial_obj.paginas,
        historial_obj.estado
      ]
      for index_col, dato in enumerate(dato_list):
        item = QTableWidgetItem(str(dato))
        self.tblLectura.setItem(index_fila, index_col, item)

  def actualizarTablaGeneros(self):
    generos = self.generoDao.listarGeneros()

    self.tblGenero.setColumnCount(2)
    self.tblGenero.setHorizontalHeaderLabels(['ID', 'Nombre'])
    self.tblGenero.setRowCount(len(generos))

    for fila, genero in enumerate(generos):
      dato = [
        genero.id_genero,
        genero.nombre_genero
      ]

      for columna, atributo in enumerate(dato):
        item = QTableWidgetItem(str(atributo))
        self.tblGenero.setItem(fila, columna, item) #Aquí el item es el atributo transformado en un item de tabla

if __name__ == "__main__":
  app = QApplication(sys.argv)

  login = DialogLogin()
  if login.exec() == QDialog.DialogCode.Accepted:
    ventana_principal = vtnPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())
  else:
    sys.exit()