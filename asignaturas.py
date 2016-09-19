import sys
#..import pymysql

from PyQt4 import QtCore, QtGui, uic, QtSql
from conn import *

class Asignaturas(QtGui.QWidget):
    '''La clase Asignaturas llevara adelante todas las operaciones referidas a inscripcion a Materias, y sus derivados'''
    def __init__(self, usr):
        super(Asignaturas, self).__init__()
        '''Instancio un objeto a la base de datos'''
        self.usr = usr
        self.Conecto_a_DB()

    def inscribir(self, dni):
        '''Creo lista para guardar los GroupBox a recorrer'''
        self.lista = []
        self.v = QtGui.QVBoxLayout()
        '''Obtengo la consulta'''
        self.dni = dni
        q = self.ObtengoCalificaciones()

        if q.size() > 0:
            '''Proceso FOBA'''
            ctrl = 1
            layFoba = self.ListoFOBA(ctrl)

            layCursos = self.ListoCursos()

            self.lista = [layFoba, layCursos]

        else:

            '''Solo puede anotarse a FOBA y a Cursos Extraprogramaticos'''
            layFoba = self.ListoFOBA()
            layCursos = self.ListoCursos()
            self.lista = [layFoba, layCursos]

        txt = QtGui.QLabel("Por favor, seleccioná las materias a las que deseas inscribirte")
        ly = QtGui.QGridLayout()
        ly.addWidget(txt, 0, 0)
        ly.sizeHint()
        self.v.addLayout(ly)
        for i in self.lista:
            self.v.addWidget(i)
        #  self.v.addWidget(layFoba)
        #  self.v.addWidget(layCursos)
        h = QtGui.QHBoxLayout()
        BtnOk = QtGui.QPushButton("&Anotar")
        BtnCancel = QtGui.QPushButton("&Limpiar")
        h.addStretch(1)
        h.addWidget(BtnOk)
        h.addWidget(BtnCancel)
        self.v.addLayout(h)
        self.control = 0
        QtCore.QObject.connect(BtnOk, QtCore.SIGNAL("clicked()"), self.anotar)
        return self.v

    def ObtengoCalificaciones(self):
        '''Busco en la tabla de Calificaciones las materias no aprobadas aún por el dni'''
        sql = "SELECT * from calificaciones WHERE alumno = :dni"
        if self.db.database('asignaturas').isOpen() is True:
            print("entre")
            q = QtSql.QSqlQuery(self.db.database('asignaturas'))
            q.prepare(sql)
            q.bindValue(":dni", self.dni)
            estado = self.ejecuto(q)
            return estado
        else:
            print("la base de datos no está abierta")
            print(self.db.database('asignaturas').lastError())

    def ListoMaterias(self, ctrl, c):
        pass


    def ListoFOBA(self, control=0):
        print(control)
        q = self.MateriasFoba(control)
        if isinstance(q, list):
            gl = self.CreoGridLista(q, "Materias FOBA")
        else:
            gl = self.CreoGrid(q, "Materias FOBA")
        gl.setObjectName("GFoba")
        print("paso por aca")
        return gl

    def ListoCursos(self):
        q = self.CursosExtraprogramaticos()
        gl = self.CreoGrid(q, "Cursos Extraprogramáticos")
        gl.setObjectName("GCursos")
        return gl

    def CreoGridLista(self, q, titulo):
        lay = QtGui.QGridLayout()
        lay.setObjectName(titulo)
        f = 0
        c = 0
        gb = QtGui.QGroupBox(titulo)
        for i in q:
            if c > 4:
                c = 0
                f = f + 1
                '''Creo el CheckBox y lo agrego al Layout'''
            ckb = QtGui.QCheckBox(i.value(1), gb)
            ckb.setObjectName(str(i.value(0)))
            print(ckb.objectName())
            lay.addWidget(ckb, f, c)
            c = c + 1
            '''seteo el layout al grid'''
#        gb = QtGui.QGroupBox(titulo)
        print("Llego acá")
        gb.setLayout(lay)
        print("Llego acá tmb")
        return gb

    def CreoGrid(self, q, titulo):
        lay = QtGui.QGridLayout()
        lay.setObjectName(titulo)
        f = 0
        c = 0
        gb = QtGui.QGroupBox(titulo)
        while q.next():
            if c > 4:
                c = 0
                f = f + 1
                '''Creo el CheckBox y lo agrego al Layout'''
            ckb = QtGui.QCheckBox(q.value(1), gb)
            ckb.setObjectName(str(q.value(0)))
            print(ckb.objectName())
            lay.addWidget(ckb, f, c)
            c = c + 1
            '''seteo el layout al grid'''
#        gb = QtGui.QGroupBox(titulo)
        gb.setLayout(lay)
        return gb

    def anotar(self):
        self.control = self.control + 1
        print("control " + str(self.control))
        self.materias = []
        '''Obtengo largo de la lista'''
        for i in self.lista:
            if isinstance(i, QtGui.QGroupBox):
                for c in i.findChildren(QtGui.QCheckBox):
                    if c.isChecked():
                        self.materias.append("(")
                        self.materias.append(c.objectName())
                        self.materias.append(", ")
                        self.materias.append(self.dni)
                        self.materias.append(")")
                        self.materias.append(", ")
        self.materias.pop()
        l = "".join(self.materias)
        print(l)
        self.anotoMaterias(self.dni, l)

    # Proceso toda la información FOBA, devuelvo una Lista con las materias
    # disponibles de FOBA para anotar al alumno
    def FOBA(self):
        '''Obtengo el total de materias FOBA'''
        sql = "SELECT * from asignaturas INNER JOIN carreras on asignaturas.carrera = carreras.id_carrera WHERE carreras.nombre = 'FOBA'"
        foba = QtSql.QSqlQuery(self.db.database('asignaturas'))
        foba.prepare(sql)
        foba = self.ejecuto(foba)
#        sql = "SELECT asignaturas.*, carreras.nombre as c, calificaciones.alumno as alumno, calificaciones.nota as nota FROM asignaturas INNER JOIN carreras on asignaturas.carrera = carreras.id_carrera INNER JOIN calificaciones on asignaturas.id_asignatura = calificaciones.id_asign WHERE carreras.nombre = :carrera AND alumno = :dni"
        sql = "SELECT * from calificaciones WHERE alumno = :dni"
        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        q.bindValue(":dni", int(self.dni))
        estado = self.ejecuto(q)
        print("Cantidad de elementos " + str(estado.size()))
        '''Proceso para presentar todas las materias FOBA disponibles para cursar'''
        if estado.size() < 8:
            l = []
            vuelta = 0
            "Agrego todas las materias"
            while foba.next():
                l.append(foba.record())
            while estado.next():
                for i in l:
                    if i.value(0) == estado.value(1):
                        self.ControloNotas()
                        l.remove(i)
        else:
            l = "FOBA Completo"
        return l

    def Chequea_Aprobado(self, f, e):
        pass

    def ObtengoMaterias(self, c):
        sql = "SELECT asignaturas.*, carreras.nombre as c FROM asignaturas INNER JOIN carreras on asignaturas.carrera = carreras.id_carrera WHERE carreras.nombre = :carrera"
        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        q.bindValue(":carrera", c)
        estado = self.ejecuto(q)
        return estado

    def MateriasFoba(self, control):
        c = 'FOBA'
        if control == 0:
            print("Control es None")
            datos = self.ObtengoMaterias(c)
        else:
            print("Control no es None")
            datos = self.FOBA()

        return datos

    def ejecuto(self, q):
            estado = q.exec_()
            pipi = q.executedQuery()
            if estado is True:
                print("estado true")
                if q.isActive() is False:
                    print("La consulta no está activa")
                else:
                    return q
            else:
#               print(dni)
                print(pipi)
                print((self.db.database('asignaturas').lastError()))


    def CursosExtraprogramaticos(self):
        c = 'Cursos Extraprogramáticos'
        datos = self.ObtengoMaterias(c)
        return datos

    def anotoMaterias(self, dni, materias):
        '''Preparo la sentencia para inscribir al alumno'''
        sql = "INSERT INTO calificaciones (id_asign, alumno) VALUES " + materias
        print(sql)
        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
#        q.bindValue(":dni", dni)
        try:
            q.exec_()
        except:
            print(self.db.database('asignaturas').lastError())
#        return estado


    def Conecto_a_DB(self):
        try:
            self.db
        except:
            conn = Connection()
            conn.SetUsuario(self.usr)

        self.db = conn.CreateConnection('asignaturas')
        if self.db.database('asignaturas').isOpen():
            print("Conexión exitosa a Asignaturas")


