import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon
def window():
    app = QApplication(sys.argv) ## uygulama oluşturur
    win = QMainWindow() ## pencere oluşturur
    win.setWindowTitle("First Application") ## uygulama başlıgını degiştirir
    win.setGeometry(200,200,500,500) ## yatayda ve dikeyde 200 piksel aşagı iner pencerenin boyutu ise 500 x 500 olur
    win.setWindowIcon(QIcon("icon.jpg")) ## uygulama başlıgına icon ekler
    win.setToolTip("my tooltip") ## uygulamanın her hangibiryerinde üzerine geldiginde ve biraz bekledigin açıklama yazısı
    win.show() ## uygulamyı çalıştırır
    sys.exit(app.exec_()) ## x => çarpı ikonuna tıklandıgı zaman uygulama durur

window()