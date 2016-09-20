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
            print(type(layFoba))
            print("Zaraza " + layFoba)
            if layFoba is True:
                self.anotoProfTec()
            elif layFoba is False:
                print("No tienes materias disponibles para la inscripción")
            else:
                self.lista.append(layFoba)
                print("layFoba no es True ni False")
            layCursos = self.ListoCursos()
            self.lista.append(layCursos)

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
        print(type(q))
        if q is True:
            print("FOBA TERMINADO")
            return True
        elif isinstance(q, str):
            print(q)
            return False
        if isinstance(q, list):
            gl = self.CreoGridLista(q, "Materias FOBA")
        elif isinstance(q, QtSql.QSqlQuery):
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
        print("Entro a FOBA")
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
        "Agrego todas las materias a la lista"
        l = []
        while foba.next():
            l.append(foba.record())

        if estado.size() < 8:
            print("Estado tiene menos de 8 elementos")

            while estado.next():
                for i in l:
                    if i.value(0) == estado.value(1):
                        l.remove(i)
        else:
            total_aprobadas = 0
            print("Estado tiene 8 elementos")
            while estado.next():
                print(estado.value(1))
                for i in l:
                    print("Value Foba " + str(i.value(0)))
                    print("Value Calif " + str(estado.value(1)))
                    if i.value(0) == estado.value(1):

                        if self.ControloNotas(estado.record()) is True:
                            total_aprobadas = total_aprobadas + 1

            if total_aprobadas == 8:
                print("Aprobo las 8 materias FOBA")
                l = True
            else:
                l = "No tiene materias disponibles para la inscripción"
        return l


    def Chequea_Aprobado(self, f, e):
        pass

    def ControloNotas(self, e):
        print("Cuatri1 " + str(e.value(2)))
        print("Cuatri2 " + str(e.value(3)))
        print("Recup " + str(e.value(4)))
        n1 = 0
        n2 = 0
        n3 = 0
        n4 = 0
        if isinstance(e.value(2), QtCore.QPyNullVariant):
            print("None N1")
            n1 = 0
        else:
            n1 = e.value(2)
        if isinstance(e.value(3), QtCore.QPyNullVariant):
            print("None N2")
            n2 = 0
        else: n2 = e.value(3)
        if isinstance(e.value(4), QtCore.QPyNullVariant):
            print("None N3")
            n3 = 0
        else:
            n3 = e.value(4)
        if isinstance(e.value(9), QtCore.QPyNullVariant):
            n4 = 0
        else:
            n4 = e.value(9)
        if n4 >= 4:
            print("Nota en Asignatura " + str(e.value(1))+ "es mayor a 4 " + str(e.value(9)))
            return True
        elif (n1 + n2 / 2) >= 4:

            return True
        elif (n1 + n3 / 2) >= 4:

            return True
        elif (n2 + n3 / 2) >= 4:

            return True
        else:
            print("Nota en Asignatura " + str(e.value(1))+ "no es mayor a 4 " + str(e.value(9)))
            return False

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

    def anotoProfTec(self):
        print("entro a AnotoProfTec")
        '''Obtengo las materias disponibles para inscribir al alumno'''
        '''Obtengo carrera del alumno'''
        sql = "SELECT carreras.id_carrera from alumnos " \
        "INNER JOIN carreras on alumnos.Carrera = carreras.nombre " \
        "WHERE DNI = :dni"
        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        q.bindValue(":dni", self.dni)
        carrera = self.ejecuto(q)
        while carrera.next():
            print(carrera.value(0))

    def Conecto_a_DB(self):
        try:
            self.db
        except:
            conn = Connection()
            conn.SetUsuario(self.usr)
            self.db = conn.CreateConnection('asignaturas')
            if self.db.database('asignaturas').isOpen():
                print("Conexión exitosa a Asignaturas")


