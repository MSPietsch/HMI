# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wizard_1(object):
    def setupUi(self, wizard_1):
        wizard_1.setObjectName("wizard_1")
        wizard_1.resize(650, 440)
        self.frame = QtWidgets.QFrame(wizard_1)
        self.frame.setGeometry(QtCore.QRect(0, 0, 650, 440))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(40, 20, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 370, 650, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.weiterButton = QtWidgets.QPushButton(self.frame)
        self.weiterButton.setGeometry(QtCore.QRect(520, 390, 120, 30))
        self.weiterButton.setObjectName("weiterButton")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(40, 90, 531, 231))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.textFeld = QtWidgets.QTextEdit(self.widget)
        self.textFeld.setObjectName("textFeld")
        self.verticalLayout.addWidget(self.textFeld)

        self.retranslateUi(wizard_1)
        QtCore.QMetaObject.connectSlotsByName(wizard_1)

    def retranslateUi(self, wizard_1):
        _translate = QtCore.QCoreApplication.translate
        wizard_1.setWindowTitle(_translate("wizard_1", "Form"))
        self.label.setText(_translate("wizard_1", "Definieren Sie die Abweichungsparameter für Knoten Nr D-1."))
        self.weiterButton.setText(_translate("wizard_1", "Weiter"))
        self.checkBox_4.setText(_translate("wizard_1", "Fluss"))
        self.checkBox_5.setText(_translate("wizard_1", "Temperatur"))
        self.checkBox_3.setText(_translate("wizard_1", "Druck"))
        self.checkBox_2.setText(_translate("wizard_1", "Unreinheiten"))
        self.checkBox_6.setText(_translate("wizard_1", "Füllstand"))
        self.checkBox.setText(_translate("wizard_1", "Isolation"))
        self.textFeld.setHtml(_translate("wizard_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-style:italic; color:#848484;\">Parameter hinzufügen...</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wizard_1 = QtWidgets.QWidget()
    ui = Ui_wizard_1()
    ui.setupUi(wizard_1)
    wizard_1.show()
    sys.exit(app.exec_())
