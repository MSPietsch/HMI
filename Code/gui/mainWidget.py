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
        mainWidget.resize(1001, 450)
        self.gridLayoutWidget = QtWidgets.QWidget(mainWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1001, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.RILabel = QtWidgets.QLabel(mainWidget)
        self.RILabel.setGeometry(QtCore.QRect(-2, -2, 991, 461))
        self.RILabel.setText("")
        self.RILabel.setPixmap(QtGui.QPixmap("RI_Fliesschema.png"))
        self.RILabel.setScaledContents(True)
        self.RILabel.setObjectName("RILabel")

        self.retranslateUi(mainWidget)
        QtCore.QMetaObject.connectSlotsByName(mainWidget)

    def retranslateUi(self, mainWidget):
        _translate = QtCore.QCoreApplication.translate
        mainWidget.setWindowTitle(_translate("mainWidget", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWidget = QtWidgets.QWidget()
    ui = Ui_mainWidget()
    ui.setupUi(mainWidget)
    mainWidget.show()
    sys.exit(app.exec_())
