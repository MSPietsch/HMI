# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard_3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wizard_3(object):
    def setupUi(self, wizard_3):
        wizard_3.setObjectName("wizard_3")
        wizard_3.resize(650, 440)
        wizard_3.setMinimumSize(QtCore.QSize(650, 440))
        wizard_3.setMaximumSize(QtCore.QSize(650, 440))
        self.frame_4 = QtWidgets.QFrame(wizard_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 650, 440))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.uberschriftLabel = QtWidgets.QLabel(self.frame_4)
        self.uberschriftLabel.setGeometry(QtCore.QRect(0, 20, 671, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uberschriftLabel.setFont(font)
        self.uberschriftLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.uberschriftLabel.setObjectName("uberschriftLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 380, 251, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.zuruckButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.zuruckButton.setEnabled(True)
        self.zuruckButton.setCheckable(False)
        self.zuruckButton.setObjectName("zuruckButton")
        self.horizontalLayout.addWidget(self.zuruckButton)
        self.weiterButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.weiterButton.setObjectName("weiterButton")
        self.horizontalLayout.addWidget(self.weiterButton)
        self.line = QtWidgets.QFrame(self.frame_4)
        self.line.setGeometry(QtCore.QRect(0, 370, 650, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 80, 641, 184))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.gridLayout = QtWidgets.QGridLayout(self.horizontalLayoutWidget_4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(180, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lineEdit_2.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 5, 1, 1)
        self.abweichungLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.abweichungLabel.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.abweichungLabel.setFont(font)
        self.abweichungLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.abweichungLabel.setObjectName("abweichungLabel")
        self.gridLayout.addWidget(self.abweichungLabel, 3, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(60, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_11.setMaximumSize(QtCore.QSize(40, 40))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../icons/Pfeil_transparent_small.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label.setMaximumSize(QtCore.QSize(180, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setMaximumSize(QtCore.QSize(180, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_10.setMaximumSize(QtCore.QSize(40, 40))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../icons/Pfeil_transparent_small.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 4, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit.setMaximumSize(QtCore.QSize(180, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 150, 150, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lineEdit.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 40)
        self.line_2 = QtWidgets.QFrame(self.frame_4)
        self.line_2.setGeometry(QtCore.QRect(187, 77, 20, 301))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_4)
        self.line_3.setGeometry(QtCore.QRect(436, 77, 20, 301))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame_4)
        self.line_4.setGeometry(QtCore.QRect(-103, 67, 871, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.retranslateUi(wizard_3)
        QtCore.QMetaObject.connectSlotsByName(wizard_3)

    def retranslateUi(self, wizard_3):
        _translate = QtCore.QCoreApplication.translate
        wizard_3.setWindowTitle(_translate("wizard_3", "Form"))
        self.uberschriftLabel.setText(_translate("wizard_3", "Abweichenung \"mehr Druck\" in Knoten Nr. D-1"))
        self.zuruckButton.setText(_translate("wizard_3", "Zurück"))
        self.weiterButton.setText(_translate("wizard_3", "Weiter"))
        self.lineEdit_2.setText(_translate("wizard_3", "3. weitere..."))
        self.abweichungLabel.setText(_translate("wizard_3", "mehr Druck"))
        self.label_6.setText(_translate("wizard_3", "Abweichung"))
        self.label_9.setText(_translate("wizard_3", "2. Schaden an Sensor K2"))
        self.label_5.setText(_translate("wizard_3", "Konsequenz"))
        self.label.setText(_translate("wizard_3", "2. zu hohe Temperatur"))
        self.label_4.setText(_translate("wizard_3", "1. Schaden am Ventil V1"))
        self.label_3.setText(_translate("wizard_3", "1. zu viel Fluss"))
        self.label_2.setText(_translate("wizard_3", "Ursache"))
        self.lineEdit.setText(_translate("wizard_3", "3. weitere..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wizard_3 = QtWidgets.QWidget()
    ui = Ui_wizard_3()
    ui.setupUi(wizard_3)
    wizard_3.show()
    sys.exit(app.exec_())
