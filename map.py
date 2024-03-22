from PyQt5 import QtCore, QtGui, QtWidgets
from ui_file.form_ui import Ui_Form

style     =    "QPushButton {font: 11px ; color: #333; border: 2px solid #555; border-radius: 20px;border-style: outset;background: #00ff7f ;}";
taxi     =     "QPushButton {font: 11px ; color: #333; border: 2px solid #555; border-radius: 20px;border-style: outset;background: #d10042 ;}";
def_style = "QPushButton {color: #a9fefe; border: 2px solid #555; border-radius: 20px;border-style: outset;background:  qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #a9fefe);padding: 5px;}QPushButton:hover {background:  qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #639595);}";


class Map_UI(QtWidgets.QWidget):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.buttons = dict()

        self.setWindowTitle("SEMANHASHT")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/icon1.png"))
        self.setWindowIcon(icon)

        self.connect_buttons()
    
    def connect_buttons(self):
        self.buttons["Chaharbagh"] = self.ui.Chaharbagh;
        self.buttons["Kashani"] = self.ui.Kashani;
        self.buttons["Allameh Jafari"] = self.ui.Allameh_Jafari;
        self.buttons["Eram-e Sabz"] = self.ui.Erame_Sabz;
        self.buttons["Meydan-e Azadi"] = self.ui.Meydane_Azadi;
        self.buttons["Ostad Mo'in"] = self.ui.Ostad_Moin;
        self.buttons["Shademan"] = self.ui.Shademan;
        self.buttons["Towhid"] = self.ui.Towhid;
        self.buttons["Meydan-e Enghelab-e Eslami"] = self.ui.Meydane_Enghelabe_Eslami;
        self.buttons["Teatr-e Shahr"] = self.ui.Teatre_shahr;
        self.buttons["Ferdowsi"] = self.ui.Ferdowsi;
        self.buttons["Darvazeh Dowlat"] = self.ui.Darvazeh_Dowlat;
        self.buttons["Darvazeh Shemiran"] = self.ui.Darvazeh_Shemiran;
        self.buttons["Meydan-e Shohada"] = self.ui.Meydane_Shohada;
        self.buttons["Ebn-e Sina"] = self.ui.Ebne_Sina;
        self.buttons["Pirouzi"] = self.ui.Pirouzi;
        self.buttons["Nabard"] = self.ui.Nabard;
        self.buttons["Nirou Havaei"] = self.ui.Nirou_Havaei;
        self.buttons["Shahid Kolahdouz"] = self.ui.Shahid_Kolahdouz;
        self.buttons["Kouhsar"] = self.ui.Kouhsar;
        self.buttons["Yadegar-e Emam"] = self.ui.Yadegare_Emam;
        self.buttons["Boostan-e laleh"] = self.ui.Bosstane_Laleh;
        self.buttons["Meydan-e Hazrat-e ValiAsr"] = self.ui.Meydane_Hazrate_Valiasr;
        self.buttons["Haftom-e Tir"] = self.ui.Haftome_Tir;
        self.buttons["Emam Hossein"] = self.ui.Emam_Hossein;
        self.buttons["Shahid Rezaei"] = self.ui.Shahid_Rezaei;
        self.buttons["Haram-e Hazrat-e Abdolazim"] = self.ui.Harame_Hazrate_Abdolazim;
        self.buttons["Bimeh"] = self.ui.Bimeh;
        self.buttons["Tehran Pars"] = self.ui.Tehran_Pars;
        self.buttons["Shahrak-e Shari'ati"] = self.ui.Shahrake_Shariati;
        self.buttons["Rahahan"] = self.ui.Rahahan;
        self.buttons["Mirdamad"] = self.ui.Mirdamad;
        self.buttons["Tajrish"] = self.ui.Tajrish;
        self.buttons["Shahid Sadr"] = self.ui.Shahid_Sadr;
        self.buttons["Khajeh Abdollah-e Ansari"] = self.ui.Khajeh_Abdollahe_Ansari;
        self.buttons["Gha'em"] = self.ui.Ghaem;
        self.buttons["Payaneh Javanmard"] = self.ui.Payaneh_Javanmard;
        self.buttons["Gheytariyeh"] = self.ui.Gheytariyeh;
        self.buttons["Gholhak"] = self.ui.Gholhak;
        self.buttons["Shahid Haghani"] = self.ui.Shahid_Haghani;
        self.buttons["Shahid Beheshti"] = self.ui.Shahid_Beheshti;
        self.buttons["Shahid Mofatteh"] = self.ui.Shahid_Mofatteh;
        self.buttons["Taleghani"] = self.ui.Taleghani;
        self.buttons["Panzdah-e Khordad"] = self.ui.Panzdahe_Khordad;
        self.buttons["Shoush"] = self.ui.Shoush;
        self.buttons["Jonoub Terminal"] = self.ui.Jonoub_Terminal;
        self.buttons["Shahr-e Rey"] = self.ui.Shahre_Rey;
        self.buttons["Kahrizak"] = self.ui.Kahrizak;
        self.buttons["Azadegan"] = self.ui.Azadegan;
        self.buttons["Zamzam"] = self.ui.Zamzam;
        self.buttons["Javadiyeh"] = self.ui.Javadie;
        self.buttons["Mahdiyeh"] = self.ui.Mahdie;
        self.buttons["Moniriyeh"] = self.ui.Moniriyeh;
        self.buttons["Meydan-e Jahad"] = self.ui.Meydane_Jahad;
        self.buttons["Merza-ye Shirazi"] = self.ui.Merzaye_Shirazi;
        self.buttons["Sohrevardi"] = self.ui.Sohrevardi;
        self.buttons["Shahid Ghodousi"] = self.ui.Shahid_Ghodousi;
        self.buttons["Shahid Zeynoddin"] = self.ui.Shahid_Zeynoddin;
        self.buttons["Aghdasiyeh"] = self.ui.Aghdasiyeh;