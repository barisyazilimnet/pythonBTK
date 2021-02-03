import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

class my_window(QMainWindow):

    def __init__(self):
        super(my_window, self).__init__()

        self.setWindowTitle("First Application") ## uygulama başlıgını degiştirir
        self.setGeometry(200,200,500,500) ## yatayda ve dikeyde 200 piksel aşagı iner pencerenin boyutu ise 500 x 500 olur
        self.setWindowIcon(QIcon("icon.jpg")) ## uygulama başlıgına icon ekler
        self.setToolTip("my tooltip") ## uygulamanın her hangibiryerinde üzerine geldiginde ve biraz bekledigin açıklama yazısı
        self.init_UI()

    def init_UI(self):

        self.lbl_name = QtWidgets.QLabel(self) ## oluşturalan pencere içerisine eklenecek
        self.lbl_name.setText("Adınız :") ## sıfıra sıfır yazı ekler
        self.lbl_name.move(50,30)## soldan saga 50 pixel gider yukarıdan aşagı 30 pixel iner
        
        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız :")
        self.lbl_surname.move(50,70)

        self.lbl_resut = QtWidgets.QLabel(self)
        self.lbl_resut.resize(300,50)
        self.lbl_resut.move(150,140)

        self.txt_name = QtWidgets.QLineEdit(self) ## text kutusu oluşturur
        self.txt_name.move(150,30)
        self.txt_name.resize(200,32) ## text kutusunun boyutunu ayarlar

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,70)
        self.txt_surname.resize(200,32)


        self.btn_save = QtWidgets.QPushButton(self) ## buton oluşturur
        self.btn_save.setText("Kaydet")
        self.btn_save.move(150,110)
        self.btn_save.clicked.connect(self.clicked) ## butona tıklanma olayını yapıyor ve tıklandıkdan sonra yapılacak işlemler için belirtilen fonskiyona gidiyor

    def clicked(self):
        self.lbl_resut.setText(f"İsim :{self.txt_name.text()} {self.txt_surname.text()}")
        
def window():
    app = QApplication(sys.argv) ## uygulama oluşturur
    win = my_window() ## pencere oluşturur
    win.show() ## uygulamyı çalıştırır
    sys.exit(app.exec_()) ## x => çarpı ikonuna tıklandıgı zaman uygulama durur

window()