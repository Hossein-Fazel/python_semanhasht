from PyQt5 import QtCore, QtGui, QtWidgets
from ui_file.form_ui import Ui_Form

import sys
from city import *

style     =    "QPushButton {font: 11px ; color: #333; border: 2px solid #555; border-radius: 20px;border-style: outset;background: #00ff7f ;}";
taxi     =     "QPushButton {font: 11px ; color: #333; border: 2px solid #555; border-radius: 20px;border-style: outset;background: #d10042 ;}";
def_style = "QPushButton {color: #a9fefe; border: 2px solid #555; border-radius: 20px;border-style: outset;background:  qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #a9fefe);padding: 5px;}QPushButton:hover {background:  qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #639595);}";


class Map_UI(QtWidgets.QWidget):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.buttons: dict[str, QtWidgets.QPushButton] = dict()
        self.ct1 = Tehran()
        try:
            self.ct1.read_from_file("line", "bus")
        except ValueError as error:
            self.show_error(error.__str__())

        self.setWindowTitle("SEMANHASHT")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/icon1.png"))
        self.setWindowIcon(icon)
        self.check_enable();
        self.connect_buttons()
    
    def connect_buttons(self):
        self.buttons["Chaharbagh"] = self.ui.Chaharbagh
        self.ui.Chaharbagh.clicked.connect(self.on_Chaharbagh_click)

        self.buttons["Kashani"] = self.ui.Kashani
        self.ui.Kashani.clicked.connect(self.on_Kashani_click)

        self.buttons["Allameh Jafari"] = self.ui.Allameh_Jafari
        self.ui.Allameh_Jafari.clicked.connect(self.on_Allameh_Jafari_click)

        self.buttons["Eram-e Sabz"] = self.ui.Erame_Sabz
        self.ui.Erame_Sabz.clicked.connect(self.on_Erame_Sabz_click)

        self.buttons["Meydan-e Azadi"] = self.ui.Meydane_Azadi
        self.ui.Meydane_Azadi.clicked.connect(self.on_Meydane_Azadi_click)

        self.buttons["Ostad Mo'in"] = self.ui.Ostad_Moin
        self.ui.Ostad_Moin.clicked.connect(self.on_Ostad_Moin_click)

        self.buttons["Shademan"] = self.ui.Shademan
        self.ui.Shademan.clicked.connect(self.on_Shademan_click)
        
        self.buttons["Towhid"] = self.ui.Towhid
        self.ui.Towhid.clicked.connect(self.on_Towhid_click)
        
        self.buttons["Meydan-e Enghelab-e Eslami"] = self.ui.Meydane_Enghelabe_Eslami
        self.ui.Meydane_Enghelabe_Eslami.clicked.connect(self.on_Meydane_Enghelabe_Eslami_click)

        self.buttons["Teatr-e Shahr"] = self.ui.Teatre_shahr
        self.ui.Teatre_shahr.clicked.connect(self.on_Teatre_shahr_click)
        
        self.buttons["Ferdowsi"] = self.ui.Ferdowsi
        self.ui.Ferdowsi.clicked.connect(self.on_Ferdowsi_click)

        self.buttons["Darvazeh Dowlat"] = self.ui.Darvazeh_Dowlat
        self.ui.Darvazeh_Dowlat.clicked.connect(self.on_Darvazeh_Dowlat_click)

        self.buttons["Darvazeh Shemiran"] = self.ui.Darvazeh_Shemiran
        self.ui.Darvazeh_Shemiran.clicked.connect(self.on_Darvazeh_Shemiran_click)

        self.buttons["Meydan-e Shohada"] = self.ui.Meydane_Shohada
        self.ui.Meydane_Shohada.clicked.connect(self.on_Meydane_Shohada_click)

        self.buttons["Ebn-e Sina"] = self.ui.Ebne_Sina
        self.ui.Ebne_Sina.clicked.connect(self.on_Ebne_Sina_click)

        self.buttons["Pirouzi"] = self.ui.Pirouzi
        self.ui.Pirouzi.clicked.connect(self.on_Pirouzi_click)

        self.buttons["Nabard"] = self.ui.Nabard
        self.ui.Nabard.clicked.connect(self.on_Nabard_click)

        self.buttons["Nirou Havaei"] = self.ui.Nirou_Havaei
        self.ui.Nirou_Havaei.clicked.connect(self.on_Nirou_Havaei_click)

        self.buttons["Shahid Kolahdouz"] = self.ui.Shahid_Kolahdouz
        self.ui.Shahid_Kolahdouz.clicked.connect(self.on_Shahid_Kolahdouz_click)
        
        self.buttons["Kouhsar"] = self.ui.Kouhsar
        self.ui.Kouhsar.clicked.connect(self.on_Kouhsar_click)

        self.buttons["Yadegar-e Emam"] = self.ui.Yadegare_Emam
        self.ui.Yadegare_Emam.clicked.connect(self.on_Yadegare_Emam_click)

        self.buttons["Boostan-e laleh"] = self.ui.Bosstane_Laleh
        self.ui.Bosstane_Laleh.clicked.connect(self.on_Bosstane_Laleh_click)

        self.buttons["Meydan-e Hazrat-e ValiAsr"] = self.ui.Meydane_Hazrate_Valiasr
        self.ui.Meydane_Hazrate_Valiasr.clicked.connect(self.on_Meydane_Hazrate_Valiasr_click)

        self.buttons["Haftom-e Tir"] = self.ui.Haftome_Tir
        self.ui.Haftome_Tir.clicked.connect(self.on_Haftome_Tir_click)

        self.buttons["Emam Hossein"] = self.ui.Emam_Hossein
        self.ui.Emam_Hossein.clicked.connect(self.on_Emam_Hossein_click)

        self.buttons["Shahid Rezaei"] = self.ui.Shahid_Rezaei
        self.ui.Shahid_Rezaei.clicked.connect(self.on_Shahid_Rezaei_click)

        self.buttons["Haram-e Hazrat-e Abdolazim"] = self.ui.Harame_Hazrate_Abdolazim
        self.ui.Harame_Hazrate_Abdolazim.clicked.connect(self.on_Harame_Hazrate_Abdolazim_click)

        self.buttons["Bimeh"] = self.ui.Bimeh
        self.ui.Bimeh.clicked.connect(self.on_Bimeh_click)

        self.buttons["Tehran Pars"] = self.ui.Tehran_Pars
        self.ui.Tehran_Pars.clicked.connect(self.on_Tehran_Pars_click)

        self.buttons["Shahrak-e Shari'ati"] = self.ui.Shahrake_Shariati
        self.ui.Shahrake_Shariati.clicked.connect(self.on_Shahrake_Shariati_click)

        self.buttons["Rahahan"] = self.ui.Rahahan
        self.ui.Rahahan.clicked.connect(self.on_Rahahan_click)

        self.buttons["Mirdamad"] = self.ui.Mirdamad
        self.ui.Mirdamad.clicked.connect(self.on_Mirdamad_click)

        self.buttons["Tajrish"] = self.ui.Tajrish
        self.ui.Tajrish.clicked.connect(self.on_Tajrish_click)

        self.buttons["Shahid Sadr"] = self.ui.Shahid_Sadr
        self.ui.Shahid_Sadr.clicked.connect(self.on_Shahid_Sadr_click)

        self.buttons["Khajeh Abdollah-e Ansari"] = self.ui.Khajeh_Abdollahe_Ansari
        self.ui.Khajeh_Abdollahe_Ansari.clicked.connect(self.on_Khajeh_Abdollahe_Ansari_click)

        self.buttons["Gha'em"] = self.ui.Ghaem
        self.ui.Ghaem.clicked.connect(self.on_Ghaem_click)

        self.buttons["Payaneh Javanmard"] = self.ui.Payaneh_Javanmard
        self.ui.Payaneh_Javanmard.clicked.connect(self.on_Payaneh_Javanmard_click)

        self.buttons["Gheytariyeh"] = self.ui.Gheytariyeh
        self.ui.Gheytariyeh.clicked.connect(self.on_Gheytariyeh_click)

        self.buttons["Gholhak"] = self.ui.Gholhak
        self.ui.Gholhak.clicked.connect(self.on_Gholhak_click)

        self.buttons["Shahid Haghani"] = self.ui.Shahid_Haghani
        self.ui.Shahid_Haghani.clicked.connect(self.on_Shahid_Haghani_click)

        self.buttons["Shahid Beheshti"] = self.ui.Shahid_Beheshti
        self.ui.Shahid_Beheshti.clicked.connect(self.on_Shahid_Beheshti_click)

        self.buttons["Shahid Mofatteh"] = self.ui.Shahid_Mofatteh
        self.ui.Shahid_Mofatteh.clicked.connect(self.on_Shahid_Mofatteh_click)

        self.buttons["Taleghani"] = self.ui.Taleghani
        self.ui.Taleghani.clicked.connect(self.on_Taleghani_click)

        self.buttons["Panzdah-e Khordad"] = self.ui.Panzdahe_Khordad
        self.ui.Panzdahe_Khordad.clicked.connect(self.on_Panzdahe_Khordad_click)

        self.buttons["Shoush"] = self.ui.Shoush
        self.ui.Shoush.clicked.connect(self.on_Shoush_click)

        self.buttons["Jonoub Terminal"] = self.ui.Jonoub_Terminal
        self.ui.Jonoub_Terminal.clicked.connect(self.on_Jonoub_Terminal_click)

        self.buttons["Shahr-e Rey"] = self.ui.Shahre_Rey
        self.ui.Shahre_Rey.clicked.connect(self.on_Shahre_Rey_click)
        
        self.buttons["Kahrizak"] = self.ui.Kahrizak
        self.ui.Kahrizak.clicked.connect(self.on_Kahrizak_click)

        self.buttons["Azadegan"] = self.ui.Azadegan
        self.ui.Azadegan.clicked.connect(self.on_Azadegan_click)

        self.buttons["Zamzam"] = self.ui.Zamzam
        self.ui.Zamzam.clicked.connect(self.on_Zamzam_click)

        self.buttons["Javadiyeh"] = self.ui.Javadie
        self.ui.Javadie.clicked.connect(self.on_Javadie_click)

        self.buttons["Mahdiyeh"] = self.ui.Mahdie
        self.ui.Mahdie.clicked.connect(self.on_Mahdie_click)

        self.buttons["Moniriyeh"] = self.ui.Moniriyeh
        self.ui.Moniriyeh.clicked.connect(self.on_Moniriyeh_click)

        self.buttons["Meydan-e Jahad"] = self.ui.Meydane_Jahad
        self.ui.Meydane_Jahad.clicked.connect(self.on_Meydane_Jahad_click)

        self.buttons["Merza-ye Shirazi"] = self.ui.Merzaye_Shirazi
        self.ui.Merzaye_Shirazi.clicked.connect(self.on_Merzaye_Shirazi_click)

        self.buttons["Sohrevardi"] = self.ui.Sohrevardi
        self.ui.Sohrevardi.clicked.connect(self.on_Sohrevardi_click)

        self.buttons["Shahid Ghodousi"] = self.ui.Shahid_Ghodousi
        self.ui.Shahid_Ghodousi.clicked.connect(self.on_Shahid_Ghodousi_click)

        self.buttons["Shahid Zeynoddin"] = self.ui.Shahid_Zeynoddin
        self.ui.Shahid_Zeynoddin.clicked.connect(self.on_Shahid_Zeynoddin_click)

        self.buttons["Aghdasiyeh"] = self.ui.Aghdasiyeh
        self.ui.Aghdasiyeh.clicked.connect(self.on_Aghdasiyeh_click)

        self.ui.reset_btn.clicked.connect(self.on_reset_btn_click)

        self.ui.Dis_btn.clicked.connect(self.cal_sp)

    def reset_style(self):
        for key, value in self.buttons.items():
            value.setStyleSheet(def_style)
        self.ui.value.setText("")

    def on_reset_btn_click(self):
        self.reset_style()
        self.ui.OR.setText("Empty");
        self.ui.DS.setText("Empty");
        self.ui.T1.setTime(QtCore.QTime(0, 0));
        self.check_enable()
        self.ui.value.setText("")


    def on_Merzaye_Shirazi_click(self):
        if self.ui.OR.text() == "Empty":
            self.ui.Merzaye_Shirazi.setStyleSheet(style)
            self.ui.OR.setText("Merza-ye Shirazi")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Merzaye_Shirazi.setStyleSheet(style)
            self.ui.DS.setText("Merza-ye Shirazi")
        self.check_enable()

    def on_Shahrake_Shariati_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Shahrake_Shariati.setStyleSheet(style)
            self.ui.OR.setText("Shahrak-e Shari'ati")
        elif self.ui.DS.text() == "Empty":
            self.ui.Shahrake_Shariati.setStyleSheet(style)
            self.ui.DS.setText("Shahrak-e Shari'ati")
        self.check_enable()

    def on_Rahahan_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Rahahan.setStyleSheet(style)

            self.ui.OR.setText("Rahahan")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Rahahan.setStyleSheet(style)

            self.ui.DS.setText("Rahahan")
        self.check_enable()

    def on_Meydane_Hazrate_Valiasr_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Meydane_Hazrate_Valiasr.setStyleSheet(style)

            self.ui.OR.setText("Meydan-e Hazrat-e ValiAsr")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Meydane_Hazrate_Valiasr.setStyleSheet(style)

            self.ui.DS.setText("Meydan-e Hazrat-e ValiAsr")
        self.check_enable()

    def on_Bosstane_Laleh_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Bosstane_Laleh.setStyleSheet(style)

            self.ui.OR.setText("Boostan-e laleh")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Bosstane_Laleh.setStyleSheet(style)

            self.ui.DS.setText("Boostan-e laleh")
        self.check_enable()

    def on_Mirdamad_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Mirdamad.setStyleSheet(style)

            self.ui.OR.setText("Mirdamad")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Mirdamad.setStyleSheet(style)

            self.ui.DS.setText("Mirdamad")
        self.check_enable()

    def on_Tajrish_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Tajrish.setStyleSheet(style)

            self.ui.OR.setText("Tajrish")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Tajrish.setStyleSheet(style)

            self.ui.DS.setText("Tajrish")
        self.check_enable()

    def on_Shahid_Sadr_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Shahid_Sadr.setStyleSheet(style)

            self.ui.OR.setText("Shahid Sadr")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Shahid_Sadr.setStyleSheet(style)

            self.ui.DS.setText("Shahid Sadr")
        self.check_enable()

    def on_Kouhsar_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Kouhsar.setStyleSheet(style)

            self.ui.OR.setText("Kouhsar")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Kouhsar.setStyleSheet(style)

            self.ui.DS.setText("Kouhsar")
        self.check_enable()

    def on_Kashani_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Kashani.setStyleSheet(style)

            self.ui.OR.setText("Kashani")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Kashani.setStyleSheet(style)

            self.ui.DS.setText("Kashani")
        self.check_enable()

    def on_Yadegare_Emam_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Yadegare_Emam.setStyleSheet(style)

            self.ui.OR.setText("Yadegar-e Emam")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Yadegare_Emam.setStyleSheet(style)

            self.ui.DS.setText("Yadegar-e Emam")
        self.check_enable()

    def on_Haftome_Tir_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Haftome_Tir.setStyleSheet(style)

            self.ui.OR.setText("Haftom-e Tir")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Haftome_Tir.setStyleSheet(style)

            self.ui.DS.setText("Haftom-e Tir")
        self.check_enable()

    def on_Emam_Hossein_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Emam_Hossein.setStyleSheet(style)

            self.ui.OR.setText("Emam Hossein")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Emam_Hossein.setStyleSheet(style)

            self.ui.DS.setText("Emam Hossein")
        self.check_enable()

    def on_Meydane_Shohada_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Meydane_Shohada.setStyleSheet(style)

            self.ui.OR.setText("Meydan-e Shohada")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Meydane_Shohada.setStyleSheet(style)

            self.ui.DS.setText("Meydan-e Shohada")
        self.check_enable()

    def on_Shahid_Rezaei_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Shahid_Rezaei.setStyleSheet(style)

            self.ui.OR.setText("Shahid Rezaei")

        elif (self.ui.DS.text() == "Empty"):
            self.ui.Shahid_Rezaei.setStyleSheet(style)

            self.ui.DS.setText("Shahid Rezaei")
        self.check_enable()

    def on_Harame_Hazrate_Abdolazim_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Harame_Hazrate_Abdolazim.setStyleSheet(style)

            self.ui.OR.setText("Haram-e Hazrat-e Abdolazim")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Harame_Hazrate_Abdolazim.setStyleSheet(style)

            self.ui.DS.setText("Haram-e Hazrat-e Abdolazim")
        self.check_enable()

    def on_Chaharbagh_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Chaharbagh.setStyleSheet(style)

            self.ui.OR.setText("Chaharbagh")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Chaharbagh.setStyleSheet(style)

            self.ui.DS.setText("Chaharbagh")
        self.check_enable()

    def on_Allameh_Jafari_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Allameh_Jafari.setStyleSheet(style)

            self.ui.OR.setText("Allameh Jafari")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Allameh_Jafari.setStyleSheet(style)

            self.ui.DS.setText("Allameh Jafari")
        self.check_enable()

    def on_Erame_Sabz_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Erame_Sabz.setStyleSheet(style)

            self.ui.OR.setText("Eram-e Sabz")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Erame_Sabz.setStyleSheet(style)

            self.ui.DS.setText("Eram-e Sabz")
        self.check_enable()

    def on_Meydane_Azadi_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Meydane_Azadi.setStyleSheet(style)

            self.ui.OR.setText("Meydan-e Azadi")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Meydane_Azadi.setStyleSheet(style)

            self.ui.DS.setText("Meydan-e Azadi")
        self.check_enable()

    def on_Ostad_Moin_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Ostad_Moin.setStyleSheet(style)

            self.ui.OR.setText("Ostad Mo'in")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Ostad_Moin.setStyleSheet(style)

            self.ui.DS.setText("Ostad Mo'in")
        self.check_enable()

    def on_Shademan_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Shademan.setStyleSheet(style)

            self.ui.OR.setText("Shademan")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Shademan.setStyleSheet(style)

            self.ui.DS.setText("Shademan")
        self.check_enable()

    def on_Towhid_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Towhid.setStyleSheet(style)

            self.ui.OR.setText("Towhid")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Towhid.setStyleSheet(style)

            self.ui.DS.setText("Towhid")
        self.check_enable()

    def on_Meydane_Enghelabe_Eslami_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Meydane_Enghelabe_Eslami.setStyleSheet(style)

            self.ui.OR.setText("Meydan-e Enghelab-e Eslami")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Meydane_Enghelabe_Eslami.setStyleSheet(style)

            self.ui.DS.setText("Meydan-e Enghelab-e Eslami")
        self.check_enable()

    def on_Teatre_shahr_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Teatre_shahr.setStyleSheet(style)

            self.ui.OR.setText("Teatr-e Shahr")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Teatre_shahr.setStyleSheet(style)

            self.ui.DS.setText("Teatr-e Shahr")
        self.check_enable()

    def on_Ferdowsi_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Ferdowsi.setStyleSheet(style)

            self.ui.OR.setText("Ferdowsi")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Ferdowsi.setStyleSheet(style)

            self.ui.DS.setText("Ferdowsi")

    def on_Darvazeh_Dowlat_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Darvazeh_Dowlat.setStyleSheet(style)

            self.ui.OR.setText("Darvazeh Dowlat")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Darvazeh_Dowlat.setStyleSheet(style)

            self.ui.DS.setText("Darvazeh Dowlat")
        self.check_enable()

    def on_Darvazeh_Shemiran_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Darvazeh_Shemiran.setStyleSheet(style)

            self.ui.OR.setText("Darvazeh Shemiran")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Darvazeh_Shemiran.setStyleSheet(style)

            self.ui.DS.setText("Darvazeh Shemiran")
        self.check_enable()

    def on_Ebne_Sina_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Ebne_Sina.setStyleSheet(style)

            self.ui.OR.setText("Ebn-e Sina")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Ebne_Sina.setStyleSheet(style)

            self.ui.DS.setText("Ebn-e Sina")
        self.check_enable()

    def on_Pirouzi_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Pirouzi.setStyleSheet(style)

            self.ui.OR.setText("Pirouzi")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Pirouzi.setStyleSheet(style)

            self.ui.DS.setText("Pirouzi")
        self.check_enable()

    def on_Nabard_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Nabard.setStyleSheet(style)

            self.ui.OR.setText("Nabard")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Nabard.setStyleSheet(style)

            self.ui.DS.setText("Nabard")
        self.check_enable()

    def on_Nirou_Havaei_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Nirou_Havaei.setStyleSheet(style)

            self.ui.OR.setText("Nirou Havaei")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Nirou_Havaei.setStyleSheet(style)

            self.ui.DS.setText("Nirou Havaei")
        self.check_enable()

    def on_Shahid_Kolahdouz_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Shahid_Kolahdouz.setStyleSheet(style)

            self.ui.OR.setText("Shahid Kolahdouz")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Shahid_Kolahdouz.setStyleSheet(style)

            self.ui.DS.setText("Shahid Kolahdouz")
        self.check_enable()

    def on_Kahrizak_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Kahrizak.setStyleSheet(style)

            self.ui.OR.setText("Kahrizak")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Kahrizak.setStyleSheet(style)
            self.ui.DS.setText("Kahrizak")
        self.check_enable()

    def on_Shahre_Rey_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Shahre_Rey.setStyleSheet(style)

            self.ui.OR.setText("Shahr-e Rey")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Shahre_Rey.setStyleSheet(style)

            self.ui.DS.setText("Shahr-e Rey")
        self.check_enable()

    def on_Jonoub_Terminal_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Jonoub_Terminal.setStyleSheet(style)

            self.ui.OR.setText("Jonoub Terminal")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Jonoub_Terminal.setStyleSheet(style)

            self.ui.DS.setText("Jonoub Terminal")
        self.check_enable()

    def on_Shoush_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Shoush.setStyleSheet(style)

            self.ui.OR.setText("Shoush")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Shoush.setStyleSheet(style)

            self.ui.DS.setText("Shoush")
        self.check_enable()

    def on_Panzdahe_Khordad_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Panzdahe_Khordad.setStyleSheet(style)

            self.ui.OR.setText("Panzdah-e Khordad")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Panzdahe_Khordad.setStyleSheet(style)

            self.ui.DS.setText("Panzdah-e Khordad")
        self.check_enable()

    def on_Taleghani_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Taleghani.setStyleSheet(style)

            self.ui.OR.setText("Taleghani")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Taleghani.setStyleSheet(style)

            self.ui.DS.setText("Taleghani")
        self.check_enable()

    def on_Shahid_Mofatteh_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Shahid_Mofatteh.setStyleSheet(style)

            self.ui.OR.setText("Shahid Mofatteh")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Shahid_Mofatteh.setStyleSheet(style)

            self.ui.DS.setText("Shahid Mofatteh")
        self.check_enable()

    def on_Shahid_Beheshti_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Shahid_Beheshti.setStyleSheet(style)

            self.ui.OR.setText("Shahid Beheshti")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Shahid_Beheshti.setStyleSheet(style)

            self.ui.DS.setText("Shahid Beheshti")
        self.check_enable()

    def on_Shahid_Haghani_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Shahid_Haghani.setStyleSheet(style)

            self.ui.OR.setText("Shahid Haghani")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Shahid_Haghani.setStyleSheet(style)

            self.ui.DS.setText("Shahid Haghani")
        self.check_enable()

    def on_Gholhak_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Gholhak.setStyleSheet(style)

            self.ui.OR.setText("Gholhak")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Gholhak.setStyleSheet(style)

            self.ui.DS.setText("Gholhak")
        self.check_enable()

    def on_Gheytariyeh_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Gheytariyeh.setStyleSheet(style)

            self.ui.OR.setText("Gheytariyeh")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Gheytariyeh.setStyleSheet(style)

            self.ui.DS.setText("Gheytariyeh")
        self.check_enable()

    def on_Meydane_Jahad_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Meydane_Jahad.setStyleSheet(style)

            self.ui.OR.setText("Meydan-e Jahad")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Meydane_Jahad.setStyleSheet(style)

            self.ui.DS.setText("Meydan-e Jahad")
        self.check_enable()

    def on_Sohrevardi_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Sohrevardi.setStyleSheet(style)

            self.ui.OR.setText("Sohrevardi")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Sohrevardi.setStyleSheet(style)

            self.ui.DS.setText("Sohrevardi")
        self.check_enable()

    def on_Shahid_Ghodousi_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Shahid_Ghodousi.setStyleSheet(style)

            self.ui.OR.setText("Shahid Ghodousi")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Shahid_Ghodousi.setStyleSheet(style)

            self.ui.DS.setText("Shahid Ghodousi")
        self.check_enable()

    def on_Shahid_Zeynoddin_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Shahid_Zeynoddin.setStyleSheet(style)

            self.ui.OR.setText("Shahid Zeynoddin")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Shahid_Zeynoddin.setStyleSheet(style)

            self.ui.DS.setText("Shahid Zeynoddin")
        self.check_enable()

    def on_Aghdasiyeh_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Aghdasiyeh.setStyleSheet(style)

            self.ui.OR.setText("Aghdasiyeh")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Aghdasiyeh.setStyleSheet(style)

            self.ui.DS.setText("Aghdasiyeh")
        self.check_enable()

    def on_Ghaem_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Ghaem.setStyleSheet(style)

            self.ui.OR.setText("Gha'em")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Ghaem.setStyleSheet(style)

            self.ui.DS.setText("Gha'em")
        self.check_enable()

    def on_Khajeh_Abdollahe_Ansari_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Khajeh_Abdollahe_Ansari.setStyleSheet(style)

            self.ui.OR.setText("Khajeh Abdollah-e Ansari")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Khajeh_Abdollahe_Ansari.setStyleSheet(style)

            self.ui.DS.setText("Khajeh Abdollah-e Ansari")
        self.check_enable()

    def on_Payaneh_Javanmard_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Payaneh_Javanmard.setStyleSheet(style)

            self.ui.OR.setText("Payaneh Javanmard")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Payaneh_Javanmard.setStyleSheet(style)

            self.ui.DS.setText("Payaneh Javanmard")
        self.check_enable()

    def on_Bimeh_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Bimeh.setStyleSheet(style)

            self.ui.OR.setText("Bimeh")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Bimeh.setStyleSheet(style)

            self.ui.DS.setText("Bimeh")
        self.check_enable()

    def on_Tehran_Pars_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Tehran_Pars.setStyleSheet(style)

            self.ui.OR.setText("Tehran Pars")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Tehran_Pars.setStyleSheet(style)

            self.ui.DS.setText("Tehran Pars")
        self.check_enable()

    def on_Mahdie_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Mahdie.setStyleSheet(style)

            self.ui.OR.setText("Mahdiyeh")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Mahdie.setStyleSheet(style)

            self.ui.DS.setText("Mahdiyeh")
        self.check_enable()

    def on_Moniriyeh_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Moniriyeh.setStyleSheet(style)

            self.ui.OR.setText("Moniriyeh")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Moniriyeh.setStyleSheet(style)

            self.ui.DS.setText("Moniriyeh")
        self.check_enable()

    def on_Javadie_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Javadie.setStyleSheet(style)

            self.ui.OR.setText("Javadiyeh")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Javadie.setStyleSheet(style)

            self.ui.DS.setText("Javadiyeh")
        self.check_enable()

    def on_Zamzam_click(self):

        if (self.ui.OR.text() == "Empty"):
            self.ui.Zamzam.setStyleSheet(style)
            self.ui.OR.setText("Zamzam")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Zamzam.setStyleSheet(style)
            self.ui.DS.setText("Zamzam")
        self.check_enable()

    def on_Azadegan_click(self):
        if (self.ui.OR.text() == "Empty"):
            self.ui.Azadegan.setStyleSheet(style)
            self.ui.OR.setText("Azadegan")
        elif (self.ui.DS.text() == "Empty"):
            self.ui.Azadegan.setStyleSheet(style)
            self.ui.DS.setText("Azadegan")
        self.check_enable()

    def check_enable(self):
        if self.ui.OR.text() != "Empty" and self.ui.DS.text() != "Empty":
            self.ui.Dis_btn.setEnabled(1)
            self.ui.Time_btn.setEnabled(1)
            self.ui.Cost_btn.setEnabled(1)
        else:
            self.ui.Dis_btn.setEnabled(0)
            self.ui.Time_btn.setEnabled(0)
            self.ui.Cost_btn.setEnabled(0)
    
    def show_clock(self, t1: Time):
        hour = 0;
        if t1.get_type().lower() == "pm" :
            hour = t1.get_hour() + 12;
        else:
            if t1.get_hour() == 12 :
                hour = 0;
            else:
                hour = t1.get_hour();

        self.ui.T1.setTime(QtCore.QTime(hour, t1.get_minute()))

    def show_error(self, ewhat:str ):
        mbox = QtWidgets.QMessageBox()
        mbox.setIconPixmap(QtGui.QPixmap("./img/error.png"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/error.png"))
        mbox.setWindowIcon(icon)
        mbox.setWindowTitle("ERROR")
        mbox.setText(ewhat)
        mbox.exec()
        sys.exit()

    def cal_sp(self):
        path = self.ct1.find_shortest_path(self.ui.OR.text(), self.ui.DS.text())
        self.show_sp(path, Time(self.ui.T1.text()))
    
    def show_sp(self,path: save_direction, t1: Time):
        self.ui.value.setText(str(path.value) + " km")

        for station in path.stations:
            self.buttons[station].setStyleSheet(style)
        
        self.show_clock(t1 + self.ct1.get_arrive_time_sp(path, t1))