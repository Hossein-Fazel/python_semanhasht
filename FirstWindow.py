from PyQt5 import QtCore, QtGui, QtWidgets
from ui_file.mainwindow_ui import Ui_MainWindow
import sys
from map import Map_UI

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        ui = Ui_MainWindow()
        ui.setupUi(self)
        self.my_map = Map_UI()

        self.setWindowTitle("SEMANHASHT")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/icon1.png"))
        self.setWindowIcon(icon)

        ui.total_exit.clicked.connect(self.open_map)

    def open_map(self):
        self.my_map.show()
        self.close()