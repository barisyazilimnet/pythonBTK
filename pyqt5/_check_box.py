# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_check_box.ui'
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
        self.btn_secilenleri_al_hobbies = QtWidgets.QPushButton(self.centralwidget)
        self.btn_secilenleri_al_hobbies.setGeometry(QtCore.QRect(110, 260, 201, 91))
        self.btn_secilenleri_al_hobbies.setObjectName("btn_secilenleri_al_hobbies")
        self.lbl_result_hobbies = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result_hobbies.setGeometry(QtCore.QRect(100, 360, 181, 151))
        self.lbl_result_hobbies.setText("")
        self.lbl_result_hobbies.setObjectName("lbl_result_hobbies")
        self.group_hobbies = QtWidgets.QGroupBox(self.centralwidget)
        self.group_hobbies.setGeometry(QtCore.QRect(130, 40, 171, 211))
        self.group_hobbies.setObjectName("group_hobbies")
        self.layoutWidget = QtWidgets.QWidget(self.group_hobbies)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 171, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_sinema = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_sinema.setObjectName("cb_sinema")
        self.verticalLayout.addWidget(self.cb_sinema)
        self.cb_read_book = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_read_book.setObjectName("cb_read_book")
        self.verticalLayout.addWidget(self.cb_read_book)
        self.cb_spor = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_spor.setObjectName("cb_spor")
        self.verticalLayout.addWidget(self.cb_spor)
        self.group_lessons = QtWidgets.QGroupBox(self.centralwidget)
        self.group_lessons.setGeometry(QtCore.QRect(550, 40, 191, 211))
        self.group_lessons.setObjectName("group_lessons")
        self.layoutWidget_2 = QtWidgets.QWidget(self.group_lessons)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 171, 201))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb_web_tasarim = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.cb_web_tasarim.setObjectName("cb_web_tasarim")
        self.verticalLayout_2.addWidget(self.cb_web_tasarim)
        self.cb_programlama = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.cb_programlama.setObjectName("cb_programlama")
        self.verticalLayout_2.addWidget(self.cb_programlama)
        self.cb_matematik = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.cb_matematik.setObjectName("cb_matematik")
        self.verticalLayout_2.addWidget(self.cb_matematik)
        self.lbl_result_lessons = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result_lessons.setGeometry(QtCore.QRect(530, 360, 181, 151))
        self.lbl_result_lessons.setText("")
        self.lbl_result_lessons.setObjectName("lbl_result_lessons")
        self.btn_secilenleri_al_lessons = QtWidgets.QPushButton(self.centralwidget)
        self.btn_secilenleri_al_lessons.setGeometry(QtCore.QRect(540, 260, 201, 91))
        self.btn_secilenleri_al_lessons.setObjectName("btn_secilenleri_al_lessons")
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
        self.btn_secilenleri_al_hobbies.setText(_translate("MainWindow", "Seçilenleri al"))
        self.group_hobbies.setTitle(_translate("MainWindow", "GroupBox"))
        self.cb_sinema.setText(_translate("MainWindow", "Sinema"))
        self.cb_read_book.setText(_translate("MainWindow", "Kitap okumak"))
        self.cb_spor.setText(_translate("MainWindow", "Spor"))
        self.group_lessons.setTitle(_translate("MainWindow", "GroupBox"))
        self.cb_web_tasarim.setText(_translate("MainWindow", "Web tasarım"))
        self.cb_programlama.setText(_translate("MainWindow", "Programlama"))
        self.cb_matematik.setText(_translate("MainWindow", "Matematik"))
        self.btn_secilenleri_al_lessons.setText(_translate("MainWindow", "Seçilenleri al"))
