import sys
from PyQt5 import QtWidgets
from _radio_button import Ui_MainWindow

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.radio_turkiye.setChecked(True) ## türkiye seçenegini seçili hale getirir
        self.ui.radio_universite.setChecked(True) ## türkiye seçenegini seçili hale getirir

        self.ui.radio_turkiye.toggled.connect(self.on_clicked_country)
        self.ui.radio_almanya.toggled.connect(self.on_clicked_country)
        self.ui.radio_azerbaycan.toggled.connect(self.on_clicked_country)
        self.ui.radio_yunanistan.toggled.connect(self.on_clicked_country)
        
        self.ui.radio_ilkokul.toggled.connect(self.on_clicked_education)
        self.ui.radio_lise.toggled.connect(self.on_clicked_education)
        self.ui.radio_universite.toggled.connect(self.on_clicked_education)
        self.ui.radio_yuksek_lisans.toggled.connect(self.on_clicked_education)

        self.ui.btn_country.clicked.connect(self.get_selected_country)
        self.ui.btn_education.clicked.connect(self.get_selected_education)

    def on_clicked_country(self):
        rb = self.sender()
        if rb.isChecked():
            print(f"Seçilen ülke :{rb.text()}")

    def on_clicked_education(self):
        rb = self.sender()
        if rb.isChecked():
            print(f"Seçilen eğitim :{rb.text()}")

    def get_selected_country(self):
        items = self.ui.groupBox_country.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lbl_country.setText(f"Seçilen ülke :{rb.text()}")

    def get_selected_education(self):
        items = self.ui.groupBox_education.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lbl_education.setText(f"Seçilen eğitim :{rb.text()}")

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

app()