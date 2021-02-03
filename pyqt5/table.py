import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from _table import Ui_MainWindow

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_products()
        self.ui.btn_save.clicked.connect(self.save_product)
        self.ui.table_products.doubleClicked.connect(self.doubleclicked) ## çift tıklandıgında onla ilgili özelliklere ulaşılabilir

    def doubleclicked(self):
        for item in self.ui.table_products.selectedItems():
            print(item.row(), item.column(), item.text())

    def save_product(self):
        name = self.ui.lbl_name.text()
        price = self.ui.lbl_price.text()

        if name and price is not None:
            row_count = self.ui.table_products.rowCount()
            self.ui.table_products.insertRow(row_count)
            self.ui.table_products.setItem(row_count,0, QTableWidgetItem(name))
            self.ui.table_products.setItem(row_count,1, QTableWidgetItem(price))

    def load_products(self):
        products = [
            {
                "name" : "Samsung S5",
                "price" : 2000
            },
            {
                "name" : "Samsung S6",
                "price" : 3000
            },
            {
                "name" : "Samsung S7",
                "price" : 4000
            },
            {
                "name" : "Samsung S8",
                "price" : 5000
            }
        ]

        # self.ui.table_products.setRowCount(3) ## tabloda 3 tane satır oluşturur
        self.ui.table_products.setRowCount(len(products)) 
        self.ui.table_products.setColumnCount(2) ## tabloda 2 kolon oluşturur
        self.ui.table_products.setHorizontalHeaderLabels(("Name","Price"))
        self.ui.table_products.setColumnWidth(0, 200)
        self.ui.table_products.setColumnWidth(1, 100)
        
        row_index = 0
        for product in products:
            self.ui.table_products.setItem(row_index,0, QTableWidgetItem(product["name"]))
            self.ui.table_products.setItem(row_index,1, QTableWidgetItem(str(product["price"])))
            row_index += 1

        # self.ui.table_products.setItem(0,0, QTableWidgetItem("Samsung S5"))
        # self.ui.table_products.setItem(0,1, QTableWidgetItem("2000"))
        # self.ui.table_products.setItem(1,0, QTableWidgetItem("Samsung S6"))
        # self.ui.table_products.setItem(1,1, QTableWidgetItem("3000"))
        # self.ui.table_products.setItem(2,0, QTableWidgetItem("Samsung S7"))
        # self.ui.table_products.setItem(2,1, QTableWidgetItem("4000"))

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

app()