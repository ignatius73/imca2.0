# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pymca.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Alumnos = QtGui.QMenu(self.menubar)
        self.menu_Alumnos.setObjectName(_fromUtf8("menu_Alumnos"))
        self.menuCooperadora = QtGui.QMenu(self.menubar)
        self.menuCooperadora.setObjectName(_fromUtf8("menuCooperadora"))
        self.menu_Estad_sticas = QtGui.QMenu(self.menubar)
        self.menu_Estad_sticas.setObjectName(_fromUtf8("menu_Estad_sticas"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Nuevo_Alumno = QtGui.QAction(MainWindow)
        self.action_Nuevo_Alumno.setObjectName(_fromUtf8("action_Nuevo_Alumno"))
        self.action_Modificar_Alumno = QtGui.QAction(MainWindow)
        self.action_Modificar_Alumno.setObjectName(_fromUtf8("action_Modificar_Alumno"))
        self.action_Listar_Alumno = QtGui.QAction(MainWindow)
        self.action_Listar_Alumno.setObjectName(_fromUtf8("action_Listar_Alumno"))
        self.action_Borrar_Alumno = QtGui.QAction(MainWindow)
        self.action_Borrar_Alumno.setObjectName(_fromUtf8("action_Borrar_Alumno"))
        self.actionC_obrar = QtGui.QAction(MainWindow)
        self.actionC_obrar.setObjectName(_fromUtf8("actionC_obrar"))
        self.actionListado_Deudores = QtGui.QAction(MainWindow)
        self.actionListado_Deudores.setObjectName(_fromUtf8("actionListado_Deudores"))
        self.action_Balance = QtGui.QAction(MainWindow)
        self.action_Balance.setObjectName(_fromUtf8("action_Balance"))
        self.actionAgregar_Gasto = QtGui.QAction(MainWindow)
        self.actionAgregar_Gasto.setObjectName(_fromUtf8("actionAgregar_Gasto"))
        self.actionIngresos = QtGui.QAction(MainWindow)
        self.actionIngresos.setObjectName(_fromUtf8("actionIngresos"))
        self.actionEgresos = QtGui.QAction(MainWindow)
        self.actionEgresos.setObjectName(_fromUtf8("actionEgresos"))
        self.actionLibro_Diario = QtGui.QAction(MainWindow)
        self.actionLibro_Diario.setObjectName(_fromUtf8("actionLibro_Diario"))
        self.actionCaja = QtGui.QAction(MainWindow)
        self.actionCaja.setObjectName(_fromUtf8("actionCaja"))
        self.actionInscri_pciones = QtGui.QAction(MainWindow)
        self.actionInscri_pciones.setObjectName(_fromUtf8("actionInscri_pciones"))
        self.menu_Alumnos.addAction(self.action_Nuevo_Alumno)
        self.menu_Alumnos.addAction(self.action_Modificar_Alumno)
        self.menu_Alumnos.addAction(self.action_Listar_Alumno)
        self.menu_Alumnos.addAction(self.action_Borrar_Alumno)
        self.menu_Alumnos.addAction(self.actionInscri_pciones)
        self.menuCooperadora.addAction(self.actionIngresos)
        self.menuCooperadora.addAction(self.actionEgresos)
        self.menuCooperadora.addAction(self.actionLibro_Diario)
        self.menuCooperadora.addAction(self.actionCaja)
        self.menubar.addAction(self.menu_Alumnos.menuAction())
        self.menubar.addAction(self.menuCooperadora.menuAction())
        self.menubar.addAction(self.menu_Estad_sticas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menu_Alumnos.setTitle(_translate("MainWindow", "&Alumnos", None))
        self.menuCooperadora.setTitle(_translate("MainWindow", "&Cooperadora", None))
        self.menu_Estad_sticas.setTitle(_translate("MainWindow", "&Estadísticas", None))
        self.action_Nuevo_Alumno.setText(_translate("MainWindow", "&Nuevo Alumno", None))
        self.action_Modificar_Alumno.setText(_translate("MainWindow", "&Modificar Alumno", None))
        self.action_Listar_Alumno.setText(_translate("MainWindow", "&Listar Alumno", None))
        self.action_Borrar_Alumno.setText(_translate("MainWindow", "&Borrar Alumno", None))
        self.actionC_obrar.setText(_translate("MainWindow", "C&obrar", None))
        self.actionListado_Deudores.setText(_translate("MainWindow", "Listado &Deudores", None))
        self.action_Balance.setText(_translate("MainWindow", "&Balance", None))
        self.actionAgregar_Gasto.setText(_translate("MainWindow", "Agregar &Gasto", None))
        self.actionIngresos.setText(_translate("MainWindow", "&Ingresos", None))
        self.actionEgresos.setText(_translate("MainWindow", "&Egresos", None))
        self.actionLibro_Diario.setText(_translate("MainWindow", "Libro &Diario", None))
        self.actionCaja.setText(_translate("MainWindow", "Ca&ja", None))
        self.actionInscri_pciones.setText(_translate("MainWindow", "Inscri&pciones", None))

