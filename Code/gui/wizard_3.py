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
        self.frame_4 = QtWidgets.QFrame(wizard_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 650, 440))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(0, 15, 671, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(9, 69, 621, 301))
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
        self.label_11.setPixmap(QtGui.QPixmap("../icons/Pfeil_transparent.png"))
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
        self.label_10.setPixmap(QtGui.QPixmap("../icons/Pfeil_transparent.png"))
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.listView_2 = QtWidgets.QListView(self.horizontalLayoutWidget_4)
        self.listView_2.setMinimumSize(QtCore.QSize(120, 0))
        self.listView_2.setObjectName("listView_2")
        self.horizontalLayout_4.addWidget(self.listView_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 380, 251, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.line = QtWidgets.QFrame(self.frame_4)
        self.line.setGeometry(QtCore.QRect(0, 370, 650, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(wizard_3)
        QtCore.QMetaObject.connectSlotsByName(wizard_3)

    def retranslateUi(self, wizard_3):
        _translate = QtCore.QCoreApplication.translate
        wizard_3.setWindowTitle(_translate("wizard_3", "Form"))
        self.label_9.setText(_translate("wizard_3", "[Bezeichnung Abweichung] in [Knotennummer name etc]"))
        self.label_12.setText(_translate("wizard_3", "Abweichung"))
        self.pushButton_2.setText(_translate("wizard_3", "Zurück"))
        self.pushButton.setText(_translate("wizard_3", "Weiter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wizard_3 = QtWidgets.QWidget()
    ui = Ui_wizard_3()
    ui.setupUi(wizard_3)
    wizard_3.show()
    sys.exit(app.exec_())
