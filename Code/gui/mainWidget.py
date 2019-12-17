# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWidget(object):
    def setupUi(self, mainWidget):
        mainWidget.setObjectName("mainWidget")
        mainWidget.resize(754, 384)
        self.label = QtWidgets.QLabel(mainWidget)
        self.label.setGeometry(QtCore.QRect(130, 140, 551, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(mainWidget)
        self.label_2.setGeometry(QtCore.QRect(250, 210, 55, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(mainWidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 60, 93, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/HAZOP.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(mainWidget)
        QtCore.QMetaObject.connectSlotsByName(mainWidget)

    def retranslateUi(self, mainWidget):
        _translate = QtCore.QCoreApplication.translate
        mainWidget.setWindowTitle(_translate("mainWidget", "Form"))
        self.label.setText(_translate("mainWidget", "Neue Ansicht"))
        self.label_2.setText(_translate("mainWidget", "Nik"))
        self.pushButton.setStatusTip(_translate("mainWidget", "Hallo Nik"))
        self.pushButton.setText(_translate("mainWidget", "Jo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWidget = QtWidgets.QWidget()
    ui = Ui_mainWidget()
    ui.setupUi(mainWidget)
    mainWidget.show()
    sys.exit(app.exec_())
