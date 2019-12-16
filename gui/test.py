# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test.ui'
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
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(210, 160, 181, 71))
        self.btn1.setObjectName("btn1")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(220, 70, 211, 41))
        self.label1.setObjectName("label1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuZwei = QtWidgets.QMenu(self.menuFile)
        self.menuZwei.setObjectName("menuZwei")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEins = QtWidgets.QAction(MainWindow)
        self.actionEins.setObjectName("actionEins")
        self.actionDrei = QtWidgets.QAction(MainWindow)
        self.actionDrei.setObjectName("actionDrei")
        self.actionTest = QtWidgets.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.menuZwei.addAction(self.actionTest)
        self.menuZwei.addSeparator()
        self.menuZwei.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionEins)
        self.menuFile.addAction(self.menuZwei.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDrei)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn1.setText(_translate("MainWindow", "Press Me!"))
        self.label1.setText(_translate("MainWindow", "Hallo mein Name ist Tim"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuZwei.setTitle(_translate("MainWindow", "Zwei"))
        self.actionEins.setText(_translate("MainWindow", "Eins"))
        self.actionDrei.setText(_translate("MainWindow", "Drei"))
        self.actionTest.setText(_translate("MainWindow", "Test"))
