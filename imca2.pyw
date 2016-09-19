#Imca2 Versión Pytq Dinámico
import sys
import pymysql
from PyQt4 import QtCore, QtGui, uic, QtSql
from inscribirAlumno import *
from conn import *

global dba
dba = Connection()
global usr, passw

#Clase ventana principal
class VentanaPrincipal(QtGui.QMainWindow):
    #Modo constructor de la clase
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui = uic.loadUi("pymca.ui", self)
        #creo boton siguiente
        self.mdi = QtGui.QMdiArea()
        '''hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        #hbox.addWidget()

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        mdi.addLayout(vbox)'''

        self.setCentralWidget(self.mdi)

        self.setGeometry(300, 300, 300, 150)
        self.ui.action_Nuevo_Alumno.triggered.connect(self.calcular)

    def calcular(self):
        print("entro")
        NextBtn = QtGui.QPushButton("&Siguiente")
        cancelBtn = QtGui.QPushButton("&Cancelar")
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(NextBtn)
        hbox.addWidget(cancelBtn)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.inscr = QtGui.QWidget()
        self.inscr.setLayout(vbox)
        self.mdi.addSubWindow(self.inscr)
        self.mdi.show()



'''        #Valido si el usuario está registrado
        self.login = Login()
        self.login.exec_()
        #Creo un layout para el contenedor mainwindow
        self.ui = uic.loadUi("pymca.ui", self)
        #Agrego un mdi area
        self.mdi = Mdi()
        self.setCentralWidget(self.mdi)'''





#Creamos la instancia para inciar app
app = QtGui.QApplication(sys.argv)
#nstanciamos una VentanaPrincipal
ventana = VentanaPrincipal()
#screenShape = QtGui.QDesktopWidget().screenGeometry()
#ventana.resize(screenShape.width(), screenShape.height())
#muestro la ventana
ventana.showMaximized()
ventana.show()
#Ejecutamos la app
app.exec_()