import sys
#..import pymysql
from PyQt4 import QtSql
from utilidades import *
from login import *


class Connection(QtSql.QSqlDatabase):

    def __init__(self):
        super(Connection, self).__init__()
        #Seteo los datos de conexión


    def SetUsuario(self, usr):
        self.usr = usr
        print("User " + self.usr[0] + " Pass " + self.usr[1])


    def GetUsuario(self):
        #  Envio tupla usuario
        return self.usr

    def CreateConnection(self, nombre = None):
        db = QtSql.QSqlDatabase.addDatabase('QMYSQL', nombre)
        db.setHostName('127.0.0.1')
        db.setDatabaseName('imca')
        db.setUserName(self.usr[0])
        db.setPassword(self.usr[1])
        print(db.connectionName())
        if db.open:
            print("base de datos conectada")
            return db
        else:
            print(db.lastError())

    def GetConnection(self):
            return self.db

    def ConsultoDNI(self, dni,db):
        '''Consulta a la DB si el alumno ya está inscripto'''

        sql = "SELECT * from alumnos WHERE DNI = :dni"
        print(sql)
        if db.database('principal').isOpen() is True:
            print("dos " + sql)
            q = QtSql.QSqlQuery(db)
            q.prepare(sql)
            q.bindValue(":dni", int(dni))
            estado = q.exec_()
            pipi = q.executedQuery()
            print(pipi)
            if estado:
                if q.isActive() is False:
                    print("La consulta no está activa")
                else:
                    if q.size() > 0:
                        print("El dni ya existe")
                        return True
                    else:
                        return False

            else:
                print(dni)
                print(pipi)
                print((db.lastError()))
        else:
            return False

    def conecto(self, usuario = None):
        # Chequeo si los datos del usuario existen
        try:
            self.usr
        except:
            print("No están disponibles los datos de usuario")
            self.SetUsuario(self)
            try:
                self.db
            except:
                self.db = self.CreateConnection(self.usr[0], self.usr[1])
                return self.db
