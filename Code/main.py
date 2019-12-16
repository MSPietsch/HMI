import os, sys

from tkinter.filedialog import askopenfilename

from gui.UI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox


##
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__connect_buttons()

    def __connect_buttons(self):
        self.ui.btnNew.clicked.connect(self.newProject)
        self.ui.btnOpen.clicked.connect(self.openProject)
        self.ui.actionNew.triggered.connect(self.newProject)
        self.ui.actionOpen.triggered.connect(self.openProject)

    #  def fkt(self):
    #     self.ui.label1.setText("Hallo ich bin der coole Malte!")
    #    print("Test!")

    # TODO Funktionen für Buttons

    def openProject(self):
        name = askopenfilename(initialdir = "../Hazops",title = "RI - Fließbild wählen",filetypes = (("PDF Dateien","*.pdf"),("Alle Dateien","*.*")))
        pass

    def newProject(self):
        try:
            os.makedirs("../Hazops/Project_X")
        except FileExistsError:
            self.showPopup("folderExists")
            pass

    def showPopup(self, info):
        if info == "folderExists":
            msg = QMessageBox()
            msg.setWindowTitle("Achtung!")
            msg.setText("Dieser Ordner existiert bereits. Bitte wählen Sie einen anderen Projektnamen.")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    print("go")
    sys.exit(app.exec_())
