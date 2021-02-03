# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_table.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table_products = QtWidgets.QTableWidget(self.centralwidget)
        self.table_products.setGeometry(QtCore.QRect(30, 30, 371, 281))
        self.table_products.setObjectName("table_products")
        self.table_products.setColumnCount(0)
        self.table_products.setRowCount(0)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(420, 30, 291, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lbl_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lbl_name.setObjectName("lbl_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lbl_name)
        self.lbl_price = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lbl_price.setObjectName("lbl_price")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lbl_price)
        self.btn_save = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_save.setObjectName("btn_save")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btn_save)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Fiyat"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
