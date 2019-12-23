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
        nodeEdit.resize(280, 320)
        nodeEdit.setMinimumSize(QtCore.QSize(280, 320))
        nodeEdit.setMaximumSize(QtCore.QSize(280, 320))
        self.centralwidget = QtWidgets.QWidget(nodeEdit)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 331, 401))
        self.widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.widget.setObjectName("widget")
        self.btn1 = QtWidgets.QPushButton(self.widget)
        self.btn1.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/cursor_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn1.setIcon(icon)
        self.btn1.setCheckable(False)
        self.btn1.setChecked(False)
        self.btn1.setAutoExclusive(True)
        self.btn1.setAutoDefault(True)
        self.btn1.setDefault(False)
        self.btn1.setFlat(False)
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.widget)
        self.btn2.setEnabled(False)
        self.btn2.setGeometry(QtCore.QRect(70, 75, 41, 41))
        self.btn2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn2.setText("")
        self.btn2.setIcon(icon)
        self.btn2.setCheckable(False)
        self.btn2.setAutoExclusive(True)
        self.btn2.setAutoDefault(True)
        self.btn2.setDefault(False)
        self.btn2.setObjectName("btn2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(70, 15, 171, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 171, 51))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(10, 175, 261, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnBin = QtWidgets.QPushButton(self.widget)
        self.btnBin.setGeometry(QtCore.QRect(20, 200, 41, 41))
        self.btnBin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnBin.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnBin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/bin_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBin.setIcon(icon1)
        self.btnBin.setIconSize(QtCore.QSize(25, 25))
        self.btnBin.setAutoExclusive(True)
        self.btnBin.setAutoDefault(True)
        self.btnBin.setDefault(False)
        self.btnBin.setFlat(False)
        self.btnBin.setObjectName("btnBin")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(70, 195, 171, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(120, 125, 171, 51))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.btn3 = QtWidgets.QPushButton(self.widget)
        self.btn3.setEnabled(False)
        self.btn3.setGeometry(QtCore.QRect(70, 130, 41, 41))
        self.btn3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/reference_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn3.setIcon(icon2)
        self.btn3.setCheckable(False)
        self.btn3.setAutoExclusive(True)
        self.btn3.setAutoDefault(True)
        self.btn3.setDefault(False)
        self.btn3.setFlat(False)
        self.btn3.setObjectName("btn3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 250, 261, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOk = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnOk.setEnabled(False)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout.addWidget(self.btnOk)
        self.btnAbort = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnAbort.setObjectName("btnAbort")
        self.horizontalLayout.addWidget(self.btnAbort)
        nodeEdit.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(nodeEdit)
        self.statusbar.setObjectName("statusbar")
        nodeEdit.setStatusBar(self.statusbar)

        self.retranslateUi(nodeEdit)
        QtCore.QMetaObject.connectSlotsByName(nodeEdit)

    def retranslateUi(self, nodeEdit):
        _translate = QtCore.QCoreApplication.translate
        nodeEdit.setWindowTitle(_translate("nodeEdit", "Knoteneditor"))
        self.btn1.setStatusTip(_translate("nodeEdit", "Markiert einen Hauptknoten."))
        self.btn2.setStatusTip(_translate("nodeEdit", "Markiert einen Nebenknoten."))
        self.label.setText(_translate("nodeEdit", "Hauptknoten markieren"))
        self.label_2.setText(_translate("nodeEdit", "Nebenknoten markieren"))
        self.btnBin.setStatusTip(_translate("nodeEdit", "Entfernt einen Knoten."))
        self.label_3.setText(_translate("nodeEdit", "Knoten entfernen"))
        self.label_4.setText(_translate("nodeEdit", "Referenzpunkt setzen"))
        self.btn3.setStatusTip(_translate("nodeEdit", "Setzt einen Referenzpunkt."))
        self.btnOk.setText(_translate("nodeEdit", "Ok"))
        self.btnAbort.setText(_translate("nodeEdit", "Abbrechen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    nodeEdit = QtWidgets.QMainWindow()
    ui = Ui_nodeEdit()
    ui.setupUi(nodeEdit)
    nodeEdit.show()
    sys.exit(app.exec_())
