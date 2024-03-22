from FirstWindow import MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()