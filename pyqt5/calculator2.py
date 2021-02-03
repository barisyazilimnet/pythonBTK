from PyQt5 import QtWidgets
import sys
from main_window import Ui_mainWindow

class App(QtWidgets.QMainWindow):

    def __init__(self):
        super(App,self).__init__()
        self.ui = Ui_mainWindow() ## main_window içindeki bütün seçeneklere ulaşılabilir
        self.ui.setupUi(self)
        self.ui.btn_toplama.clicked.connect(self.hesapla)
        self.ui.btn_cikarma.clicked.connect(self.hesapla)
        self.ui.btn_carpma.clicked.connect(self.hesapla)
        self.ui.btn_bolme.clicked.connect(self.hesapla)

    def hesapla(self):
        sender = self.sender() ##♣ hangi butona basıldıgını anlar
        result = 0
        if sender.text() == "Toplama":
            result = int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text())
        elif sender.text() == "Çıkarma":    
            result = int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text())
        elif sender.text() == "Çarpma":
            result = int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text())
        elif sender.text() == "Bölme":
            result = int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text())

        self.ui.lbl_sonuc.setText(f"Sonuç :{result}")

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())

app()
