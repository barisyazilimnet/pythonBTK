import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from _msg_box import Ui_MainWindow

class my_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_app, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_exit.clicked.connect(self.show_dialog)

    def show_dialog(self):
        result = QMessageBox.question(self, "Close Application", "Are you sure?", QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore, QMessageBox.Cancel)
        ## self /dialogun başlıgı /dialogun içindeki mesaj /olmasını istediginiz buton veya butonlar /seçili olarak gelmesini istediginiz buton
        if result == QMessageBox.Ok:
            QtWidgets.qApp.quit()
            
    #     msg = QMessageBox() ## butona tıklandıgı zaman dialog kutusu oluşmasını saglar

    #     msg.setWindowTitle("Close Application")  ## oluşan dialog kutusunun ismi
    #     msg.setText("Are you sure?") ## oluşan dialog kutusundaki mesaj
        
    #     ## oluşan dialog kutusunda ki oluşacak olan icon
    #     # msg.setIcon(QMessageBox.Question) 
    #     msg.setIcon(QMessageBox.Warning) 
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore) ## butonlar oluşturulabilir
    #     msg.setDefaultButton(QMessageBox.Cancel) ## buton seçili olarak gelir
    #     msg.setDetailedText("details...") ## detay butonuna basıldıgında detayları gösterir
    #     msg.buttonClicked.connect(self.popup_button)
    #     x = msg.exec_() ## çıkan dialog kutusunun kapanması için

    # def popup_button(self, i):

    #     if i.text() == "OK":
    #         QtWidgets.qApp.quit() ## ok butonuna basılınca form kapatılır
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

app()