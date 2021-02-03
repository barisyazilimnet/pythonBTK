# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_list.ui'
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
        self.list_items = QtWidgets.QListWidget(self.centralwidget)
        self.list_items.setGeometry(QtCore.QRect(40, 30, 401, 441))
        self.list_items.setObjectName("list_items")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(470, 30, 221, 441))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_add = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout.addWidget(self.btn_add)
        self.btn_edit = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_edit.setObjectName("btn_edit")
        self.verticalLayout.addWidget(self.btn_edit)
        self.btn_delete = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_delete.setObjectName("btn_delete")
        self.verticalLayout.addWidget(self.btn_delete)
        self.btn_up = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_up.setObjectName("btn_up")
        self.verticalLayout.addWidget(self.btn_up)
        self.btn_down = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_down.setObjectName("btn_down")
        self.verticalLayout.addWidget(self.btn_down)
        self.btn_sort = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_sort.setObjectName("btn_sort")
        self.verticalLayout.addWidget(self.btn_sort)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_exit = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
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
        self.btn_add.setText(_translate("MainWindow", "Add"))
        self.btn_edit.setText(_translate("MainWindow", "Edit"))
        self.btn_delete.setText(_translate("MainWindow", "Delete"))
        self.btn_up.setText(_translate("MainWindow", "Up"))
        self.btn_down.setText(_translate("MainWindow", "Down"))
        self.btn_sort.setText(_translate("MainWindow", "Sort"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
