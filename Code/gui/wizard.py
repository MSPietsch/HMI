# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName("Wizard")
        Wizard.setEnabled(True)
        Wizard.resize(687, 435)
        Wizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        Wizard.setOptions(QtWidgets.QWizard.HelpButtonOnRight|QtWidgets.QWizard.IndependentPages|QtWidgets.QWizard.NoBackButtonOnStartPage)
        Wizard.setTitleFormat(QtCore.Qt.PlainText)
        Wizard.setSubTitleFormat(QtCore.Qt.PlainText)
        self.ParamPage = QtWidgets.QWizardPage()
        self.ParamPage.setEnabled(True)
        self.ParamPage.setTitle("")
        self.ParamPage.setObjectName("ParamPage")
        self.frame = QtWidgets.QFrame(self.ParamPage)
        self.frame.setGeometry(QtCore.QRect(0, 0, 681, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 0, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(270, 140, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(270, 180, 331, 41))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 90, 332, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_7 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        Wizard.addPage(self.ParamPage)
        self.LeitwortPage = QtWidgets.QWizardPage()
        self.LeitwortPage.setObjectName("LeitwortPage")
        self.frame_2 = QtWidgets.QFrame(self.LeitwortPage)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 681, 381))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(1, 1, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1, 111, 261, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(311, 111, 263, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_17 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_17.setFont(font)
        self.checkBox_17.setObjectName("checkBox_17")
        self.gridLayout_3.addWidget(self.checkBox_17, 5, 1, 1, 1)
        self.checkBox_19 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_19.setFont(font)
        self.checkBox_19.setObjectName("checkBox_19")
        self.gridLayout_3.addWidget(self.checkBox_19, 6, 1, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_14.setFont(font)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout_3.addWidget(self.checkBox_14, 4, 0, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_3.addWidget(self.checkBox_10, 1, 0, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_15.setFont(font)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout_3.addWidget(self.checkBox_15, 5, 0, 1, 1)
        self.checkBox_20 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_20.setFont(font)
        self.checkBox_20.setObjectName("checkBox_20")
        self.gridLayout_3.addWidget(self.checkBox_20, 0, 0, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_3.addWidget(self.checkBox_9, 2, 1, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_13.setFont(font)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout_3.addWidget(self.checkBox_13, 3, 1, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_16.setFont(font)
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout_3.addWidget(self.checkBox_16, 4, 1, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout_3.addWidget(self.checkBox_12, 3, 0, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_3.addWidget(self.checkBox_8, 2, 0, 1, 1)
        self.checkBox_18 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_18.setFont(font)
        self.checkBox_18.setObjectName("checkBox_18")
        self.gridLayout_3.addWidget(self.checkBox_18, 6, 0, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_3.addWidget(self.checkBox_11, 1, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 621, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        Wizard.addPage(self.LeitwortPage)
        self.CauseConsequencePage = QtWidgets.QWizardPage()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CauseConsequencePage.setFont(font)
        self.CauseConsequencePage.setObjectName("CauseConsequencePage")
        self.frame_4 = QtWidgets.QFrame(self.CauseConsequencePage)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 681, 381))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(0, 30, 671, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(9, 69, 661, 301))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.listView = QtWidgets.QListView(self.horizontalLayoutWidget_4)
        self.listView.setMinimumSize(QtCore.QSize(120, 0))
        self.listView.setObjectName("listView")
        self.horizontalLayout_4.addWidget(self.listView)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_11.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../icons/Pfeil.png"))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_10.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../icons/Pfeil.png"))
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.listView_2 = QtWidgets.QListView(self.horizontalLayoutWidget_4)
        self.listView_2.setMinimumSize(QtCore.QSize(120, 0))
        self.listView_2.setObjectName("listView_2")
        self.horizontalLayout_4.addWidget(self.listView_2)
        Wizard.addPage(self.CauseConsequencePage)
        self.SafeguardPage = QtWidgets.QWizardPage()
        self.SafeguardPage.setObjectName("SafeguardPage")
        self.frame_3 = QtWidgets.QFrame(self.SafeguardPage)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 651, 371))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 120, 651, 80))
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
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
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
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(100, 60, 451, 89))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_3.addWidget(self.textEdit_3)
        spacerItem = QtWidgets.QSpacerItem(178, 71, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.textEdit_2 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_3.addWidget(self.textEdit_2)
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setGeometry(QtCore.QRect(180, 100, 20, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_3.setFont(font)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame_3)
        self.line_4.setGeometry(QtCore.QRect(450, 90, 16, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_4.setFont(font)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.checkBox_21 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_21.setGeometry(QtCore.QRect(400, 310, 171, 20))
        self.checkBox_21.setObjectName("checkBox_21")
        self.line_3.raise_()
        self.line_4.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.checkBox_21.raise_()
        Wizard.addPage(self.SafeguardPage)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        _translate = QtCore.QCoreApplication.translate
        Wizard.setWindowTitle(_translate("Wizard", "Hazop Designer"))
        self.label.setText(_translate("Wizard", "Definieren Sie die Parameter für Knoten X."))
        self.label_2.setText(_translate("Wizard", "Parameter hinzufügen:"))
        self.checkBox_3.setText(_translate("Wizard", "Druck"))
        self.checkBox_5.setText(_translate("Wizard", "Temperatur"))
        self.checkBox_6.setText(_translate("Wizard", "Füllstand"))
        self.checkBox_4.setText(_translate("Wizard", "Fluss"))
        self.checkBox_2.setText(_translate("Wizard", "Unreinheiten"))
        self.checkBox.setText(_translate("Wizard", "Isolation"))
        self.checkBox_7.setText(_translate("Wizard", "hier muss noch irgendwie generierter hin"))
        self.label_3.setText(_translate("Wizard", "Definieren Sie die Leitworte für die Parameter."))
        self.checkBox_17.setText(_translate("Wizard", "Danach"))
        self.checkBox_19.setText(_translate("Wizard", "Langsamer"))
        self.checkBox_14.setText(_translate("Wizard", "Früher"))
        self.checkBox_10.setText(_translate("Wizard", "Mehr"))
        self.checkBox_15.setText(_translate("Wizard", "Zuvor"))
        self.checkBox_20.setText(_translate("Wizard", "Nein, nicht"))
        self.checkBox_9.setText(_translate("Wizard", "Teilweise"))
        self.checkBox_13.setText(_translate("Wizard", "Anders als"))
        self.checkBox_16.setText(_translate("Wizard", "Später"))
        self.checkBox_12.setText(_translate("Wizard", "Umkehrung"))
        self.checkBox_8.setText(_translate("Wizard", "Sowohl als auch"))
        self.checkBox_18.setText(_translate("Wizard", "Schneller"))
        self.checkBox_11.setText(_translate("Wizard", "Weniger"))
        self.label_4.setText(_translate("Wizard", "Parameter auswählen:"))
        self.label_5.setText(_translate("Wizard", "Leitwörter auswählen:"))
        self.label_9.setText(_translate("Wizard", "[Bezeichnung Abweichung] in [Knotennummer name etc]"))
        self.label_12.setText(_translate("Wizard", "Abweichung"))
        self.label_7.setText(_translate("Wizard", "Cause X"))
        self.label_6.setText(_translate("Wizard", "Deviation X"))
        self.label_8.setText(_translate("Wizard", "Consequence X"))
        self.textEdit_3.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Safeguard1</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Safeguard2</span></p></body></html>"))
        self.checkBox_21.setText(_translate("Wizard", "Keine Safeguards"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wizard = QtWidgets.QWizard()
    ui = Ui_Wizard()
    ui.setupUi(Wizard)
    Wizard.show()
    sys.exit(app.exec_())
