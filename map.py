from PyQt5 import QtCore, QtGui, QtWidgets
from ui_file.form_ui import Ui_Form

class Map_UI(QtWidgets.QWidget):
    def __init__(self, parent= None):
        super().__init__(parent)
        ui = Ui_Form()
        ui.setupUi(self)

        self.setWindowTitle("SEMANHASHT")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/icon1.png"))
        self.setWindowIcon(icon)
