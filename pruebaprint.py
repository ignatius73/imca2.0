import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
      def __init__(self, app):
          QtGui.QMainWindow.__init__(self)
          self.app=app
          self.label=QtGui.QLabel("Print test")
          self.setCentralWidget(self.label)
      def goPrinter(self):
          printer=QtGui.QPrinter()
          dialog = QtGui.QPrintDialog(printer, self)
          if(dialog.exec_() != QtGui.QDialog.Accepted):
              return
          printLabel = QtGui.QLabel("Hello my printer.")
          painter = QtGui.QPainter(printer)
          printLabel.render(painter)
          painter.end()

#if __name__ == "__main__":
#      import sys
app = QtGui.QApplication(sys.argv)
window=MainWindow(app)
window.show()
QtCore.QTimer.singleShot(1000, window.goPrinter)
#ui.show()
app.exec_()
