import sys, re
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox, QWidget

class Utilidades():

    def __init__(self):
        super(Utilidades, self).__init__()

    def validar_vacios(self, i):
        #  Valido si el campo está vacío
        if i.text() == "":
            i.setStyleSheet("background-color: cyan")
            p = QtCore.QPoint()
            p.setX = 50
            p.setY = 82
            QtGui.QToolTip.showText(p, "No puede estar vacío", i)
            return False
        else:
            return True

    def Confirmar(self, t):
        '''Muestra Cuadro de dialogo para la confirmacion. Recibe el texto a mostrar'''
        '''Creo el Cuadro de dialogo'''
        w = QtGui.QWidget()
        v = QMessageBox.question(w, "Atención", t, QMessageBox.Ok | QMessageBox.Cancel)
        w.show()
        return v