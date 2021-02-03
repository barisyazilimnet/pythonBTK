# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_combo_box.ui'
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
        self.cb_sehirler = QtWidgets.QComboBox(self.centralwidget)
        self.cb_sehirler.setGeometry(QtCore.QRect(118, 51, 191, 61))
        self.cb_sehirler.setObjectName("cb_sehirler")
        self.lbl_result = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result.setGeometry(QtCore.QRect(330, 60, 121, 51))
        self.lbl_result.setText("")
        self.lbl_result.setObjectName("lbl_result")
        self.btn_get_item = QtWidgets.QPushButton(self.centralwidget)
        self.btn_get_item.setGeometry(QtCore.QRect(120, 130, 201, 61))
        self.btn_get_item.setObjectName("btn_get_item")
        self.btn_load_item = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_item.setGeometry(QtCore.QRect(340, 130, 211, 61))
        self.btn_load_item.setObjectName("btn_load_item")
        self.btn_clear_item = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear_item.setGeometry(QtCore.QRect(120, 210, 201, 61))
        self.btn_clear_item.setObjectName("btn_clear_item")
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
        self.btn_get_item.setText(_translate("MainWindow", "get item"))
        self.btn_load_item.setText(_translate("MainWindow", "load item"))
        self.btn_clear_item.setText(_translate("MainWindow", "clear item"))
