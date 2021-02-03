import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from _list import Ui_MainWindow

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # load students
        self.load_students()

        # add new student
        self.ui.btn_add.clicked.connect(self.add_student)

        # edit student
        self.ui.btn_edit.clicked.connect(self.edit_student)

        # delete student
        self.ui.btn_delete.clicked.connect(self.delete_student)

        # up 
        self.ui.btn_up.clicked.connect(self.up_student)
        
        # down 
        self.ui.btn_down.clicked.connect(self.down_student)

        # sort 
        self.ui.btn_sort.clicked.connect(self.sort_students)
        
        # exit 
        self.ui.btn_exit.clicked.connect(self.close_app)
        
    def load_students(self):
        self.ui.list_items.addItems(["Ahmet","Ali","Çınar"])
        self.ui.list_items.setCurrentRow(0) ## sıfırıncı indexdeki eleman seçili gelir

    def add_student(self):
        current_index = self.ui.list_items.currentRow()
        ## getText => isim bilgisi felan girilebilir
        ## getInt => sayı bilgisi girilebilir
        ## getDouble => noktalı sayı bilgisi girilebilir
        ## getItem => combobox gibi ilgili veriler girilebilir
        text, ok = QInputDialog.getText(self, "New Student", "Student Name") ## girilen bilgi text in içine atar / dönen cevabı ise ok içine atar
        if ok and text is not None:
            # self.ui.list_items.insertItem(0, text)
            self.ui.list_items.insertItem(current_index, text)

    def edit_student(self):
        index = self.ui.list_items.currentRow()
        item = self.ui.list_items.item(index)

        if item is not None:
            text, ok = QInputDialog.getText(self, "Edit Student", "Student Name", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)

    def delete_student(self):
        index = self.ui.list_items.currentRow()
        item = self.ui.list_items.item(index)
        
        if item is None:
            return

        q = QMessageBox.question(self, "Delete student", f"Do you want to delete student :{item.text()}", QMessageBox.Yes | QMessageBox.No)
        if q == QMessageBox.Yes:
            item = self.ui.list_items.takeItem(index)
            del item
    
    def up_student(self):
        index = self.ui.list_items.currentRow()
        if index >= 1:
            item = self.ui.list_items.takeItem(index)
            self.ui.list_items.insertItem(index-1, item)
            self.ui.list_items.setCurrentItem(item)

    def down_student(self):
        index = self.ui.list_items.currentRow()
        if index < self.ui.list_items.count() - 1:
            item = self.ui.list_items.takeItem(index)
            self.ui.list_items.insertItem(index + 1, item)
            self.ui.list_items.setCurrentItem(item)

    def sort_students(self):
        self.ui.list_items.sortItems()

    def close_app(self):
        quit()
                
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

app()