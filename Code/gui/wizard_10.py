# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard_10.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wizard_10(object):
    def setupUi(self, wizard_10):
        wizard_10.setObjectName("wizard_10")
        wizard_10.resize(650, 440)
        wizard_10.setMinimumSize(QtCore.QSize(650, 440))
        wizard_10.setMaximumSize(QtCore.QSize(650, 440))
        self.frame_2 = QtWidgets.QFrame(wizard_10)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 650, 440))
        self.frame_2.setMinimumSize(QtCore.QSize(650, 440))
        self.frame_2.setMaximumSize(QtCore.QSize(650, 440))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(15, 10, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(0, 370, 650, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_6 = QtWidgets.QFrame(self.frame_2)
        self.line_6.setGeometry(QtCore.QRect(-30, 40, 871, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 377, 651, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.zuruckButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.zuruckButton.setEnabled(True)
        self.zuruckButton.setMinimumSize(QtCore.QSize(115, 0))
        self.zuruckButton.setCheckable(False)
        self.zuruckButton.setObjectName("zuruckButton")
        self.horizontalLayout.addWidget(self.zuruckButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem1)
        self.weiterButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.weiterButton.setMinimumSize(QtCore.QSize(115, 0))
        self.weiterButton.setObjectName("weiterButton")
        self.horizontalLayout.addWidget(self.weiterButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 97, 231, 59))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(330, 100, 301, 250))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_20 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_20.setFont(font)
        self.checkBox_20.setObjectName("checkBox_20")
        self.gridLayout.addWidget(self.checkBox_20, 0, 0, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setCheckable(True)
        self.checkBox_10.setChecked(True)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 1, 0, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setChecked(True)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 1, 1, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 2, 0, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 2, 1, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 3, 0, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_13.setFont(font)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout.addWidget(self.checkBox_13, 3, 1, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_14.setFont(font)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout.addWidget(self.checkBox_14, 4, 0, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_16.setFont(font)
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout.addWidget(self.checkBox_16, 4, 1, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_15.setFont(font)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout.addWidget(self.checkBox_15, 5, 0, 1, 1)
        self.checkBox_17 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_17.setFont(font)
        self.checkBox_17.setObjectName("checkBox_17")
        self.gridLayout.addWidget(self.checkBox_17, 5, 1, 1, 1)
        self.checkBox_18 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_18.setFont(font)
        self.checkBox_18.setObjectName("checkBox_18")
        self.gridLayout.addWidget(self.checkBox_18, 6, 0, 1, 1)
        self.checkBox_19 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_19.setFont(font)
        self.checkBox_19.setObjectName("checkBox_19")
        self.gridLayout.addWidget(self.checkBox_19, 6, 1, 1, 1)
        self.groupBox1 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox1.setGeometry(QtCore.QRect(39, 169, 231, 141))
        self.groupBox1.setObjectName("groupBox1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.groupBox1)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_7.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_13 = QtWidgets.QLabel(self.groupBox1)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_13.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(40, 65, 154, 21))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(330, 65, 166, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setGeometry(QtCore.QRect(40, 169, 231, 40))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(74, 324, 162, 30))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(47, 329, 81, 20))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(wizard_10)
        QtCore.QMetaObject.connectSlotsByName(wizard_10)

    def retranslateUi(self, wizard_10):
        _translate = QtCore.QCoreApplication.translate
        wizard_10.setWindowTitle(_translate("wizard_10", "Form"))
        self.label_3.setText(_translate("wizard_10", "Definieren Sie die Leitwörter."))
        self.zuruckButton.setText(_translate("wizard_10", "Zurück"))
        self.weiterButton.setText(_translate("wizard_10", "Weiter"))
        self.label_2.setText(_translate("wizard_10", "Temperatur"))
        self.checkBox_20.setText(_translate("wizard_10", "Nein, nicht"))
        self.checkBox_10.setText(_translate("wizard_10", "Mehr"))
        self.checkBox_11.setText(_translate("wizard_10", "Weniger"))
        self.checkBox_8.setText(_translate("wizard_10", "Sowohl als auch"))
        self.checkBox_9.setText(_translate("wizard_10", "Teilweise"))
        self.checkBox_12.setText(_translate("wizard_10", "Umkehrung"))
        self.checkBox_13.setText(_translate("wizard_10", "Anders als"))
        self.checkBox_14.setText(_translate("wizard_10", "Früher"))
        self.checkBox_16.setText(_translate("wizard_10", "Später"))
        self.checkBox_15.setText(_translate("wizard_10", "Zuvor"))
        self.checkBox_17.setText(_translate("wizard_10", "Danach"))
        self.checkBox_18.setText(_translate("wizard_10", "Schneller"))
        self.checkBox_19.setText(_translate("wizard_10", "Langsamer"))
        self.label_4.setText(_translate("wizard_10", "Alle Parameter:"))
        self.label_7.setText(_translate("wizard_10", "Druck ✓ "))
        self.label_13.setText(_translate("wizard_10", "Temperatur"))
        self.label.setText(_translate("wizard_10", "Aktueller Parameter:"))
        self.label_5.setText(_translate("wizard_10", "Leitwörter auswählen:"))
        self.pushButton.setText(_translate("wizard_10", "Parameter entfernen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wizard_10 = QtWidgets.QWidget()
    ui = Ui_wizard_10()
    ui.setupUi(wizard_10)
    wizard_10.show()
    sys.exit(app.exec_())