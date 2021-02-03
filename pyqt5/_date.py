import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, QDateTime, QTime
from date import Ui_MainWindow

class window(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_calculate.clicked.connect(self.calculate)

    def calculate(self):
        start = self.ui.date_start.date()
        end = self.ui.date_end.date()
        print(start, end)
        # print(f"Days in month :{start.daysInMonth()}") ## bulunan ay içerisinde kaç gün oldugunu söler
        # print(f"Days in year :{start.daysInYear()}") ## bulunan yıl içerisinde kaç gün oldugunu söler
        # print(f"Total days :{start.daysTo(end)}") ## iki tarih arasındaki gün sayısını verir

        now = QDate.currentDate() ## şuan ki tarihi söler
        print(f"Total days from now :{start.daysTo(now)}") ## girilen tarihle bügünkü tarih arasındaki gün sayısını verir


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

app()