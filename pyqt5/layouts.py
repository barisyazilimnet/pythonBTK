import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self,color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)  ## oluşturulan widget arkaplanını otomatik olarak boyar
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class main_window(QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        self.setGeometry(100,100,500,500)

        # layout = QtWidgets.QVBoxLayout() ## yatay bloklar oluşturur
        # layout.addWidget(Color("red"))
        # layout.addWidget(Color("blue"))
        # layout.addWidget(Color("green"))

        hlayout = QtWidgets.QHBoxLayout() ## dikey bloklar oluşturur
        hlayout.addWidget(Color("red"))
        hlayout.addWidget(Color("blue"))
        hlayout.addWidget(Color("yellow"))
        # hlayout.setContentsMargins(50,0,0,0) ## çevresinde boşluk oluşturur
        # hlayout.setSpacing(50) # elemanlar arası boşluk oluşturur

        hlayout2 = QtWidgets.QHBoxLayout() ## dikey bloklar oluşturur
        hlayout2.addWidget(Color("red"))
        hlayout2.addWidget(Color("yellow"))

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addLayout(hlayout2)

        # layout = QtWidgets.QGridLayout()
        # layout.addWidget(Color("red"),0,0)
        # layout.addWidget(Color("blue"),1,0)
        # layout.addWidget(Color("green"),0,2)
        # layout.addWidget(Color("yellow"),3,1)


        widget = QWidget()
        widget.setLayout(vlayout)

        # widget = Color("blue")
        self.setCentralWidget(widget)

def app():
    app = QApplication(sys.argv)
    win = main_window()
    win.show()
    sys.exit(app.exec_())

app()