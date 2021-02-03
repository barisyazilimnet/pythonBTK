import sys
from PyQt5 import QtWidgets
from _combo_box import Ui_MainWindow

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ## örnek 1
        # self.ui.cb_sehirler.addItem("Ankara") ## combo box a ekleme yapar
        # self.ui.cb_sehirler.addItem("İstanbul")
        # self.ui.cb_sehirler.addItem("İzmir")

        ## örnek 2
        # cb = self.ui.cb_sehirler
        # cb.addItem("Ankara")
        # cb.addItem("İstanbul")
        # cb.addItem("İzmir")

        ## örnek 3
        # cb = self.ui.cb_sehirler
        # cb.addItems(["Ankara", "İstanbul", "İzmir"])

        self.ui.btn_load_item.clicked.connect(self.load_item) ## btuona her tıklandıgında combo boxa elemanları ekler
        self.ui.btn_get_item.clicked.connect(self.get_item)
        self.ui.btn_clear_item.clicked.connect(self.clear_item) ## butun elemanları siler
        self.ui.cb_sehirler.currentIndexChanged.connect(self.selected_changed_index) ## seçili olan elemanın index numarasını verir
        self.ui.cb_sehirler.currentIndexChanged[str].connect(self.selected_changed_text) ## seçili olan elemanın ismini numarasını verir

    def load_item(self):
        sehirler = ["Antalya", "Kocaeli", "Gaziantep", "Kilis"]
        self.ui.cb_sehirler.addItems(sehirler)

    def get_item(self):
        print(self.ui.cb_sehirler.currentText()) ## seçili olan sehrin ismini verir
        print(self.ui.cb_sehirler.currentIndex()) ## seçili olan şehrin index numarasını verir

    def selected_changed_index(self,index):
        print(index)

    def selected_changed_text(self,text):
        print(text)

    def clear_item(self):
        self.ui.cb_sehirler.clear()

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

app()