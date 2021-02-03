import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class main_form(QMainWindow):
    
    def __init__(self):
        super(main_form, self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.init_UI()
    
    def init_UI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("Sayı 1 :")
        self.lbl_sayi1.move(50,30)
        
        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)
        
        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayı 2 :")
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Toplama")
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.hesapla)
        
        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText("Çıkarma")
        self.btn_cikar.move(150,170)
        self.btn_cikar.clicked.connect(self.hesapla)

        
        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText("Çarpma")
        self.btn_carp.move(150,210)
        self.btn_carp.clicked.connect(self.hesapla)

        
        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText("Bölme")
        self.btn_bol.move(150,250)
        self.btn_bol.clicked.connect(self.hesapla)

        
        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText("Sonuç :")
        self.lbl_sonuc.move(150,290)

    def hesapla(self):
        sender = self.sender() ##♣ hangi butona basıldıgını anlar
        result = 0
        if sender.text() == "Toplama":
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender.text() == "Çıkarma":    
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender.text() == "Çarpma":
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        elif sender.text() == "Bölme":
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())

        self.lbl_sonuc.setText(f"Sonuç :{result}")
    
def app():
    app = QApplication(sys.argv)
    win = main_form()
    win.show()
    sys.exit(app.exec_())

app()