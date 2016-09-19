import sys
import pymysql
from PyQt4 import QtCore, QtGui, uic, QtSql



def CreateConnection():
    db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName('127.0.0.1')
    db.setDatabaseName('imca')
    db.setUserName('root')
    db.setPassword('schonberg')
    return db

class Inscripciones(QtGui.QWidget):
#Class Inscripciones - Inscribe a los alumnos.
    def __init__(self):
        super(Inscripciones, self).__init__()
        '''Cargo el archivo ui'''
        self.ui = uic.loadUi("inscriptos.ui", self)
        self.ui.lnCiclo.setText("2016")
        self.db = CreateConnection()
        QtCore.QObject.connect(self.BtnOk, QtCore.SIGNAL("clicked()"), self.IngresaAlumno)


    def IngresaAlumno(self):
        self.Nombre = self.lnNombre.text()
        self.carrera = self.cBCarrera.currentText()
        self.anio = self.lnCiclo.text()
        self.sexo = self.cBSexo.currentText()
        self.edad = self.sBEdad.text()
        self.dni = self.lnDni.text()
        self.fenac = self.dENac.text()
        self.lunac = self.lnLugar.text()
        self.civil = self.cBCivil.currentText()
        self.hijos = self.cBHijos.currentText()
        self.familia = self.lnFamiliar.text()
        self.calle = self.lnCalle.text()
        self.numero = self.lnNum.text()
        self.piso = self.lnPiso.text()
        self.depto = self.lnDepto.text()
        self.local = self.lnLocal.text()
        self.partido = self.lnPartido.text()
        self.cp = self.lnCP.text()
        self.tel = self.lnTel.text()
        self.movil = self.lnMov.text()
        self.mail = self.lnMail.text()
        self.titulo = self.lntitulo.text()
        self.egreso = self.dEEgr.text()
        self.escuela = self.lnEscuela.text()
        self.distrito = self.lnDistrito.text()
        self.otros = self.lnOtros.text()
        self.insti1 = self.lnInsti1.text()
        self.insti2 = self.lnInsti2.text()
        if self.rBtnSi.isChecked() == True:
            self.trab = 1
        else:
            self.trab = 0
        self.activ = self.lnAct.text()
        self.horario = self.lnHorario.text()
        self.os = self.lnOS.text()
        self.emergencia = self.lnTelEmer.text()
        if self.cBDni.isChecked():
            self.fotoDni = 1
        else:
            fotoDni = 0
        if self.cBTit.isChecked():
            self.fotoTit = 1
        else:
            self.fotoTit = 0
        if self.cBReg.isChecked():
            self.numReg = 1
        else:
            self.numreg = 0
        if self.cBFoto.isChecked():
            self.fotos = 1
        else:
            self.fotos = 0
        if self.cBCert.isChecked():
            self.certif = 1
        else:
            self.certif = 0
        self.Insertar()

    def Insertar(self):
        estado = self.db.open()
        if estado == False:
            print("Damned world")
        #Preparo la cadena sql
        sql = "INSERT INTO alumnos (NOMBRE) VALUES (:nombre)"
        #Creo el objeto para hacer la consulta
        q = QtSql.QSqlQuery()
        q.prepare(sql)
        print(self.Nombre)
        q.bindValue(":nombre", self.Nombre)
        estado = q.exec_()
        pipi = q.executedQuery()
        if estado == True:
            print("tudobom")
        else:
            print(self.dni)
            print(pipi)
            print((q.lastError()))
            print((self.db.lastError()))
        self.db.close()

#Creamos la instancia para inciar app
app = QtGui.QApplication(sys.argv)
#nstanciamos una VentanaPrincipal
ventana = Inscripciones()
#muestro la ventana
ventana.show()
#Ejecutamos la app
app.exec_()
