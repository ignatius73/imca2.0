import sys
#..import pymysql

from PyQt4 import QtCore, QtGui, uic, QtSql
from conn import *
from utilidades import *

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
            print("Zaraza " + str(layFoba))
            if layFoba is True:
                layCarrera = self.anotoProfTec()
                self.lista.append(layCarrera)
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
        '''Lista todas las posibilidades de presentación de materias FOBA''' \
        '''Devuelve un QGroupBox'''
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

########################################################################

    def ListoCursos(self):
        '''Crea un GroupBox con todas las cursos disponibles''' \
        '''Devuelve un GroupBox'''
        q = self.CursosExtraprogramaticos()
        gl = self.CreoGrid(q, "Cursos Extraprogramáticos")
        gl.setObjectName("GCursos")
        return gl

#########################################################################

    def CreoGridLista(self, q, titulo):
        '''Crea un GridLayout. Recibe un List y devuelve un GroupBox'''
        lay = QtGui.QGridLayout()
        lay.setObjectName(titulo)
        f = 0
        c = 0
        gb = QtGui.QGroupBox(titulo)
        for i in q:
            if c == 4:
                c = 0
                f = f + 1
                '''Creo el CheckBox y lo agrego al Layout'''
            ckb = QtGui.QCheckBox(i.value(1), gb)
            ckb.setObjectName(str(i.value(0)))

            lay.addWidget(ckb, f, c)
            c = c + 1
            '''seteo el layout al grid'''
#        gb = QtGui.QGroupBox(titulo)

        gb.setLayout(lay)

        return gb

#############################################################################

    def CreoGrid(self, q, titulo):
        '''Crea un GridLayout. Recibe un QtSql.SqlQuery devuelve un GroupBox'''
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

            lay.addWidget(ckb, f, c)
            c = c + 1
            '''seteo el layout al grid'''
#        gb = QtGui.QGroupBox(titulo)
        gb.setLayout(lay)
        return gb

##############################################################################

    def anotar(self):
        '''Ejecuta la consulta de inserción de materias para el alumno'''
        self.control = self.control + 1

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

#############################################################################

    def FOBA(self):
        '''Proceso toda la información FOBA, devuelvo una Lista con las''' \
        '''materias disponibles de FOBA para anotar al alumno'''
        '''Obtengo el total de materias FOBA'''

        sql = "SELECT * from asignaturas INNER JOIN carreras on " \
        "asignaturas.carrera = carreras.id_carrera WHERE "\
        "carreras.nombre = 'FOBA'"

        foba = QtSql.QSqlQuery(self.db.database('asignaturas'))
        foba.prepare(sql)
        foba = self.ejecuto(foba)

        sql = "SELECT * from calificaciones WHERE alumno = :dni"
        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        q.bindValue(":dni", int(self.dni))
        estado = self.ejecuto(q)
        l = []
        while foba.next():
            l.append(foba.record())

        if estado.size() < 8:
            while estado.next():
                for i in l:
                    if i.value(0) == estado.value(1):
                        l.remove(i)
        else:
            total_aprobadas = 0

            while estado.next():
                print(estado.value(1))
                for i in l:
                    if i.value(0) == estado.value(1):
                        if self.ControloNotas(estado.record()) is True:
                            total_aprobadas = total_aprobadas + 1

            if total_aprobadas == 8:
                l = True
            else:
                l = "No tiene materias disponibles para la inscripción"
        return l

##############################################################################

    def ControloNotas(self, e):

        n1 = 0
        n2 = 0
        n3 = 0
        n4 = 0
        if isinstance(e.value(2), QtCore.QPyNullVariant):

            n1 = 0
        else:
            n1 = e.value(2)
        if isinstance(e.value(3), QtCore.QPyNullVariant):

            n2 = 0
        else: n2 = e.value(3)
        if isinstance(e.value(4), QtCore.QPyNullVariant):

            n3 = 0
        else:
            n3 = e.value(4)
        if isinstance(e.value(9), QtCore.QPyNullVariant):
            n4 = 0
        else:
            n4 = e.value(9)
        if n4 >= 4:

            return True
        elif (n1 + n2 / 2) >= 4:

            return True
        elif (n1 + n3 / 2) >= 4:

            return True
        elif (n2 + n3 / 2) >= 4:

            return True
        else:

            return False

##############################################################################

    def ObtengoMaterias(self, c, d = 0):
        sql = "SELECT asignaturas.*, carreras.nombre as c FROM asignaturas " \
        "INNER JOIN carreras on asignaturas.carrera = carreras.id_carrera " \
        "WHERE carreras.nombre = :carrera OR carreras.nombre = :carrera2"
        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        q.bindValue(":carrera", c)
        if d != 0:
            print("No es distinto de 0")
            q.bindValue(":carrera2", d)
        else:
            q.bindValue(":carrera2", c)
        estado = self.ejecuto(q)
        return estado

##############################################################################

    def MateriasFoba(self, control):
        c = 'FOBA'
        if control == 0:
            print("Control es None")
            datos = self.ObtengoMaterias(c)
        else:
            print("Control no es None")
            datos = self.FOBA()

        return datos

##############################################################################

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
                print(pipi)
                print((self.db.database('asignaturas').lastError()))

##############################################################################

    def CursosExtraprogramaticos(self):
        c = 'Cursos Extraprogramáticos'
        datos = self.ObtengoMaterias(c)
        return datos

##############################################################################

    def anotoMaterias(self, dni, materias):
        '''Preparo la sentencia para inscribir al alumno'''
        sql = "INSERT INTO calificaciones (id_asign, alumno) " \
        "VALUES " + materias
        print(sql)
        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        self.close()
        try:
            q.exec_()
        except:
            print(self.db.database('asignaturas').lastError())

##############################################################################

    def anotoProfTec(self):
        '''Obtengo las materias disponibles para inscribir al alumno'''

        print("entro a AnotoProfTec")

        '''Obtengo carrera del alumno'''

        sql = "SELECT carreras.nombre from carreras " \
        "INNER JOIN alumnos on alumnos.Carrera = carreras.nombre " \
        "WHERE DNI = :dni"

        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        q.bindValue(":dni", self.dni)
        carrera = self.ejecuto(q)
        while carrera.next():
            carre = carrera.value(0)
        mtr = self.ObtengoMaterias(carre, 'AMBAS')
        self.util = Utilidades()
        mat = self.util.Convierto_a_Lista(mtr)
        materias = self.Limpio_Lista(mat)
        gl = self.CreoGridLista(materias,carre)
        gl.setObjectName('G' + carre)
        return gl


##############################################################################

    def Conecto_a_DB(self):
        try:
            self.db
        except:
            conn = Connection()
            conn.SetUsuario(self.usr)
            self.db = conn.CreateConnection('asignaturas')
            if self.db.database('asignaturas').isOpen():
                print("Conexión exitosa a Asignaturas")

##############################################################################

    def Limpio_Lista(self, l):
        '''Recibe una lista, busca aprobadas, correlativas, devuelve las''' \
        '''disponibles para que se anote el alumno'''

        '''Busco las materias anotadas de la carrera en las que el alumno''' \
        '''ya se encuentra anotado'''

        sql = "SELECT * FROM calificaciones WHERE alumno = :dni"
        q = QtSql.QSqlQuery(self.db.database('asignaturas'))
        q.prepare(sql)
        q.bindValue(":dni", self.dni)
        calificaciones = self.ejecuto(q)
        calif = self.util.Convierto_a_Lista(calificaciones)

        if isinstance(l, list):
            for c in calif:
                print("Calificaciones " + str(c.value(1)))
                for i in l:
                    print ("Asignatura " + str(i.value(0)) + " " + str(i.value(1)))
                    if i.value(0) == c.value(1):
                            l.remove(i)
                    else:
                        corre = self.Correlativas(i.value(3), calif)
                        if corre is False:
                            l.remove(i)


        else:
            print("No me diste una Lista")
        return l

##############################################################################

    def Correlativas(self, co, ca):
        print(co)
        if isinstance(co, QtCore.QPyNullVariant):
            return True
        else:
            return False
