# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Start.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(999, 512)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/HAZOP.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startFrame = QtWidgets.QFrame(self.centralwidget)
        self.startFrame.setGeometry(QtCore.QRect(-10, 10, 1031, 471))
        font = QtGui.QFont()
        font.setFamily("Myriad CAD")
        font.setPointSize(14)
        font.setUnderline(False)
        self.startFrame.setFont(font)
        self.startFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.startFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.startFrame.setObjectName("startFrame")
        self.label = QtWidgets.QLabel(self.startFrame)
        self.label.setGeometry(QtCore.QRect(10, -60, 1021, 511))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../icons/HazopMan_medium.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btnOpen = QtWidgets.QPushButton(self.startFrame)
        self.btnOpen.setGeometry(QtCore.QRect(290, 320, 449, 59))
        font = QtGui.QFont()
        font.setFamily("Myriad CAD")
        font.setPointSize(12)
        font.setUnderline(False)
        self.btnOpen.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/Open_project_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpen.setIcon(icon1)
        self.btnOpen.setObjectName("btnOpen")
        self.btnNew = QtWidgets.QPushButton(self.startFrame)
        self.btnNew.setGeometry(QtCore.QRect(290, 380, 449, 59))
        font = QtGui.QFont()
        font.setFamily("Myriad CAD")
        font.setPointSize(12)
        font.setUnderline(False)
        self.btnNew.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/new_project_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNew.setIcon(icon2)
        self.btnNew.setObjectName("btnNew")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 999, 26))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        self.menuAnsicht = QtWidgets.QMenu(self.menubar)
        self.menuAnsicht.setObjectName("menuAnsicht")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setIcon(icon2)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/save_project_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionAlle_Knoten_zeigen = QtWidgets.QAction(MainWindow)
        self.actionAlle_Knoten_zeigen.setCheckable(True)
        self.actionAlle_Knoten_zeigen.setChecked(False)
        self.actionAlle_Knoten_zeigen.setEnabled(False)
        self.actionAlle_Knoten_zeigen.setObjectName("actionAlle_Knoten_zeigen")
        self.actionKnoteneditor = QtWidgets.QAction(MainWindow)
        self.actionKnoteneditor.setEnabled(False)
        self.actionKnoteneditor.setObjectName("actionKnoteneditor")
        self.actionExportieren_als_Tabelle = QtWidgets.QAction(MainWindow)
        self.actionExportieren_als_Tabelle.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/export_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExportieren_als_Tabelle.setIcon(icon4)
        self.actionExportieren_als_Tabelle.setObjectName("actionExportieren_als_Tabelle")
        self.menuDatei.addAction(self.actionNew)
        self.menuDatei.addAction(self.actionOpen)
        self.menuDatei.addAction(self.actionSave)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionExportieren_als_Tabelle)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionClose)
        self.menuAnsicht.addAction(self.actionKnoteneditor)
        self.menuAnsicht.addSeparator()
        self.menuAnsicht.addAction(self.actionAlle_Knoten_zeigen)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuAnsicht.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hazop-MANTool"))
        self.btnOpen.setStatusTip(_translate("MainWindow", "Öffnet ein Projekt."))
        self.btnOpen.setText(_translate("MainWindow", "    Projekt Öffnen Ctrl+O"))
        self.btnNew.setStatusTip(_translate("MainWindow", "Erstellt ein neues Projekt."))
        self.btnNew.setText(_translate("MainWindow", "    Neues Projekt Ctrl+N"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.menuAnsicht.setTitle(_translate("MainWindow", "Knoten"))
        self.actionNew.setText(_translate("MainWindow", "Neues Projekt"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Erstellt ein neues Projekt."))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Projekt Öffnen"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Öffnet ein Projekt."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Projekt Speichern"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Speichert das aktuelle Projekt."))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionClose.setText(_translate("MainWindow", "Schließen"))
        self.actionClose.setStatusTip(_translate("MainWindow", "Schließt das Programm."))
        self.actionAlle_Knoten_zeigen.setText(_translate("MainWindow", "Alle Knoten zeigen"))
        self.actionAlle_Knoten_zeigen.setStatusTip(_translate("MainWindow", "Zeigt Knotenrahmen permanent an."))
        self.actionAlle_Knoten_zeigen.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionKnoteneditor.setText(_translate("MainWindow", "Knoteneditor öffnen"))
        self.actionKnoteneditor.setToolTip(_translate("MainWindow", "Knoteneditor"))
        self.actionKnoteneditor.setStatusTip(_translate("MainWindow", "Öffnet den Knoteneditor."))
        self.actionKnoteneditor.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionExportieren_als_Tabelle.setText(_translate("MainWindow", "Exportieren als Tabelle"))
        self.actionExportieren_als_Tabelle.setShortcut(_translate("MainWindow", "Ctrl+Shift+E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
