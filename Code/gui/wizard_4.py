# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard_4.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wizard_4(object):
    def setupUi(self, wizard_4):
        wizard_4.setObjectName("wizard_4")
        wizard_4.resize(650, 440)
        self.frame_3 = QtWidgets.QFrame(wizard_4)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 650, 440))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 220, 631, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line.setMaximumSize(QtCore.QSize(120, 16777215))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 150, 631, 71))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(120, 71, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.sg1textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sg1textEdit.sizePolicy().hasHeightForWidth())
        self.sg1textEdit.setSizePolicy(sizePolicy)
        self.sg1textEdit.setMaximumSize(QtCore.QSize(120, 60))
        self.sg1textEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sg1textEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhPreferUppercase)
        self.sg1textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sg1textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sg1textEdit.setObjectName("sg1textEdit")
        self.horizontalLayout_3.addWidget(self.sg1textEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.sg2textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sg2textEdit.sizePolicy().hasHeightForWidth())
        self.sg2textEdit.setSizePolicy(sizePolicy)
        self.sg2textEdit.setMaximumSize(QtCore.QSize(120, 60))
        self.sg2textEdit.setObjectName("sg2textEdit")
        self.horizontalLayout_3.addWidget(self.sg2textEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setGeometry(QtCore.QRect(190, 190, 20, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_3.setFont(font)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame_3)
        self.line_4.setGeometry(QtCore.QRect(446, 180, 16, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_4.setFont(font)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame_3)
        self.line_5.setGeometry(QtCore.QRect(0, 370, 650, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.labelUberschrift = QtWidgets.QLabel(self.frame_3)
        self.labelUberschrift.setGeometry(QtCore.QRect(17, 10, 630, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelUberschrift.setFont(font)
        self.labelUberschrift.setObjectName("labelUberschrift")
        self.line_6 = QtWidgets.QFrame(self.frame_3)
        self.line_6.setGeometry(QtCore.QRect(-130, 40, 871, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(-1, 375, 651, 61))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.zuruckButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.zuruckButton.setEnabled(True)
        self.zuruckButton.setMinimumSize(QtCore.QSize(115, 0))
        self.zuruckButton.setCheckable(False)
        self.zuruckButton.setObjectName("zuruckButton")
        self.horizontalLayout_2.addWidget(self.zuruckButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.zuruckButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.zuruckButton_2.setEnabled(True)
        self.zuruckButton_2.setMinimumSize(QtCore.QSize(115, 0))
        self.zuruckButton_2.setCheckable(False)
        self.zuruckButton_2.setObjectName("zuruckButton_2")
        self.horizontalLayout_2.addWidget(self.zuruckButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.weiterButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.weiterButton.setMinimumSize(QtCore.QSize(115, 0))
        self.weiterButton.setObjectName("weiterButton")
        self.horizontalLayout_2.addWidget(self.weiterButton)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.line_3.raise_()
        self.line_4.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.line_5.raise_()
        self.labelUberschrift.raise_()
        self.line_6.raise_()
        self.horizontalLayoutWidget_4.raise_()

        self.retranslateUi(wizard_4)
        QtCore.QMetaObject.connectSlotsByName(wizard_4)

    def retranslateUi(self, wizard_4):
        _translate = QtCore.QCoreApplication.translate
        wizard_4.setWindowTitle(_translate("wizard_4", "Form"))
        self.label_7.setText(_translate("wizard_4", "zu viel Fluss"))
        self.label_6.setText(_translate("wizard_4", "mehr Druck"))
        self.label_8.setText(_translate("wizard_4", "Schaden am Ventil V1"))
        self.sg1textEdit.setHtml(_translate("wizard_4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Ventil V3</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"><br /></span></p></body></html>"))
        self.sg2textEdit.setHtml(_translate("wizard_4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-style:italic; color:#a7a7a7;\">Safeguard 2</span></p></body></html>"))
        self.labelUberschrift.setText(_translate("wizard_4", "Definieren Sie die Safeguards."))
        self.zuruckButton.setText(_translate("wizard_4", "Zurück"))
        self.zuruckButton_2.setText(_translate("wizard_4", "Keine Safeguards"))
        self.weiterButton.setText(_translate("wizard_4", "Weiter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wizard_4 = QtWidgets.QWidget()
    ui = Ui_wizard_4()
    ui.setupUi(wizard_4)
    wizard_4.show()
    sys.exit(app.exec_())
