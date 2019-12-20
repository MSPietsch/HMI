# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NodeEdit.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_nodeEdit(object):
    def setupUi(self, nodeEdit):
        nodeEdit.setObjectName("nodeEdit")
        nodeEdit.resize(280, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(nodeEdit.sizePolicy().hasHeightForWidth())
        nodeEdit.setSizePolicy(sizePolicy)
        nodeEdit.setMinimumSize(QtCore.QSize(280, 200))
        nodeEdit.setMaximumSize(QtCore.QSize(280, 200))
        self.widget = QtWidgets.QWidget(nodeEdit)
        self.widget.setGeometry(QtCore.QRect(0, 0, 331, 281))
        self.widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.widget.setObjectName("widget")
        self.btnMaus1 = QtWidgets.QPushButton(self.widget)
        self.btnMaus1.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.btnMaus1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnMaus1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnMaus1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/cursor_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMaus1.setIcon(icon)
        self.btnMaus1.setAutoExclusive(True)
        self.btnMaus1.setAutoDefault(True)
        self.btnMaus1.setObjectName("btnMaus1")
        self.btnMaus2 = QtWidgets.QPushButton(self.widget)
        self.btnMaus2.setGeometry(QtCore.QRect(70, 75, 41, 41))
        self.btnMaus2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnMaus2.setText("")
        self.btnMaus2.setIcon(icon)
        self.btnMaus2.setCheckable(False)
        self.btnMaus2.setAutoExclusive(True)
        self.btnMaus2.setAutoDefault(False)
        self.btnMaus2.setObjectName("btnMaus2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(70, 15, 171, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 171, 51))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(10, 120, 261, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnBin = QtWidgets.QPushButton(self.widget)
        self.btnBin.setGeometry(QtCore.QRect(20, 145, 41, 41))
        self.btnBin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnBin.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnBin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/bin_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBin.setIcon(icon1)
        self.btnBin.setIconSize(QtCore.QSize(25, 25))
        self.btnBin.setAutoExclusive(True)
        self.btnBin.setAutoDefault(False)
        self.btnBin.setFlat(False)
        self.btnBin.setObjectName("btnBin")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 171, 51))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(nodeEdit)
        QtCore.QMetaObject.connectSlotsByName(nodeEdit)

    def retranslateUi(self, nodeEdit):
        _translate = QtCore.QCoreApplication.translate
        nodeEdit.setWindowTitle(_translate("nodeEdit", "Knoteneditor"))
        self.btnMaus1.setStatusTip(_translate("nodeEdit", "Markiert einen Hauptknoten."))
        self.btnMaus2.setStatusTip(_translate("nodeEdit", "Markiert einen Nebenknoten."))
        self.label.setText(_translate("nodeEdit", "Hauptknoten auswählen"))
        self.label_2.setText(_translate("nodeEdit", "Nebenknoten auswählen"))
        self.btnBin.setStatusTip(_translate("nodeEdit", "Entfernt einen Knoten."))
        self.label_3.setText(_translate("nodeEdit", "Knoten entfernen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    nodeEdit = QtWidgets.QWidget()
    ui = Ui_nodeEdit()
    ui.setupUi(nodeEdit)
    nodeEdit.show()
    sys.exit(app.exec_())
