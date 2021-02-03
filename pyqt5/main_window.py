# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(311, 292)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 41, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 41, 21))
        self.label_2.setObjectName("label_2")
        self.txt_sayi1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi1.setGeometry(QtCore.QRect(60, 10, 200, 32))
        self.txt_sayi1.setObjectName("txt_sayi1")
        self.txt_sayi2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi2.setGeometry(QtCore.QRect(60, 50, 200, 32))
        self.txt_sayi2.setObjectName("txt_sayi2")
        self.btn_toplama = QtWidgets.QPushButton(self.centralwidget)
        self.btn_toplama.setGeometry(QtCore.QRect(60, 100, 91, 41))
        self.btn_toplama.setObjectName("btn_toplama")
        self.btn_cikarma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikarma.setGeometry(QtCore.QRect(160, 100, 91, 41))
        self.btn_cikarma.setObjectName("btn_cikarma")
        self.btn_bolme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bolme.setGeometry(QtCore.QRect(160, 150, 91, 41))
        self.btn_bolme.setObjectName("btn_bolme")
        self.btn_carpma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carpma.setGeometry(QtCore.QRect(60, 150, 91, 41))
        self.btn_carpma.setObjectName("btn_carpma")
        self.lbl_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sonuc.setGeometry(QtCore.QRect(60, 200, 181, 41))
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 311, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("mainWindow", "Sayı 1"))
        self.label_2.setText(_translate("mainWindow", "Sayı 2"))
        self.btn_toplama.setText(_translate("mainWindow", "Toplama"))
        self.btn_cikarma.setText(_translate("mainWindow", "Çıkarma"))
        self.btn_bolme.setText(_translate("mainWindow", "Bölme"))
        self.btn_carpma.setText(_translate("mainWindow", "Çarpma"))
        self.lbl_sonuc.setText(_translate("mainWindow", "Sonuç :"))
