import sys
from PyQt5 import QtWidgets
from _check_box import Ui_MainWindow

class my_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_app, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cb_sinema.stateChanged.connect(self.show_state) ## butona tıklandıgı veya tıklanmadıgı zamanki degerleri gösterir 
                                                                ## tıklandıgı zaman 2 degerini verir tıklanmadıgı zaman 0 degerini verir
        self.ui.cb_read_book.stateChanged.connect(self.show_state)
        self.ui.cb_spor.stateChanged.connect(self.show_state)        

        self.ui.btn_secilenleri_al_hobbies.clicked.connect(self.get_all_hobbies)
        self.ui.btn_secilenleri_al_lessons.clicked.connect(self.get_all_lessons)

    def get_all_hobbies(self):
        result = ""
        items = self.ui.group_hobbies.findChildren(QtWidgets.QCheckBox) ## formdaki checkboxları getirir. checkbox yerine form elemanlarının hepsi yazılabilir
        for cb in items:
            if cb.isChecked(): ## sadece seçili olan checkboxları alır
                # print(cb.text())
                # print(cb.isChecked())
                result += cb.text() + "\n" ## seçilenlerin ismi result listesine atar

        self.ui.lbl_result_hobbies.setText(result) ## result listenin belirlenen label bölgesinde gösterilir 

    def get_all_lessons(self):
        result = ""
        items = self.ui.group_lessons.findChildren(QtWidgets.QCheckBox) ## formdaki checkboxları getirir. checkbox yerine form elemanlarının hepsi yazılabilir
        for cb in items:
            if cb.isChecked(): ## sadece seçili olan checkboxları alır
                # print(cb.text())
                # print(cb.isChecked())
                result += cb.text() + "\n" ## seçilenlerin ismi result listesine atar

        self.ui.lbl_result_lessons.setText(result) ## result listenin belirlenen label bölgesinde gösterilir 

    def show_state(self, value):
        cb = self.sender()
        print(cb.text())
        print(cb.isChecked())
    #     print(value)
        # print(self.ui.cb_sinema.isChecked()) ## seçildimi seçilmedigmi kontrol eder eger seçildiyse true bilgisi verir
        # print(self.ui.cb_sinema.text())
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

app()