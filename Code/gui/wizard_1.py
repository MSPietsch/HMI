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
        self.label.setGeometry(QtCore.QRect(15, 10, 591, 31))
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
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(59, 71, 531, 286))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_6 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.textFeld = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textFeld.sizePolicy().hasHeightForWidth())
        self.textFeld.setSizePolicy(sizePolicy)
        self.textFeld.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textFeld.setObjectName("textFeld")
        self.verticalLayout.addWidget(self.textFeld)
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(-130, 40, 871, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

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
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.textFeld.setPlaceholderText(_translate("wizard_1", "Parameter hinzufügen..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wizard_1 = QtWidgets.QWidget()
    ui = Ui_wizard_1()
    ui.setupUi(wizard_1)
    wizard_1.show()
    sys.exit(app.exec_())
