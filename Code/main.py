import os, sys

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

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
        self.ui.actionClose.triggered.connect(self.closeProject)

    #  def fkt(self):
    #     self.ui.label1.setText("Hallo ich bin der coole Malte!")
    #    print("Test!")

    # TODO Funktionen für Buttons

    def openProject(self):
        Tk().withdraw()  # nur ein Fenster wird geöffnet
        name = askopenfilename(initialdir="../Hazops", title="RI - Fließbild wählen",
                               filetypes=(("PDF Dateien", "*.pdf"), ("Alle Dateien", "*.*")))
        pass

    def newProject(self):
        Tk().withdraw()  # nur ein Fenster wird geöffnet
        directory = askdirectory(
            title="Projektspeicherort auswählen",
            mustexist=1
        )
        if directory:
            # Falls ein Pfad ausgewählt wurde muss ein RI-Fließschema ausgewählt werden
            Tk().withdraw()  # nur ein Fenster wird geöffnet
            name = askopenfilename(initialdir="../Hazops", title="RI - Fließschema wählen",
                                   filetypes=(("PDF Dateien", "*.pdf"), ("Alle Dateien", "*.*")))
            # TODO Kopiere RI in den Pfad- ist aber auch schon Backend.. lieber mal mit PDF Reader etc vielleicht machen
        # try:
        #     os.makedirs("../Hazops/Project_X")
        #
        # except FileExistsError:
        #     self.showPopup("folderExists")
        pass

    def closeProject(self):
        self.showPopup("save")

    def showPopup(self, info):
        msg = QMessageBox()
        if info == "folderExists":
            msg.setWindowTitle("Achtung!")
            msg.setText("Dieser Ordner existiert bereits. Bitte wählen Sie einen anderen Projektnamen.")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        if info == "save":
            msg.setWindowTitle("Achtung!")
            msg.setText("Möchten Sie Ihr Projekt vor dem Schließen speichern?")
            msg.setIcon(QMessageBox.Question)  # Fragezeichenlogo
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # Yes/No/ Cancel- Buttons sollen erscheinen
            # Übersetzung der Buttons ins Deutsche
            buttonY = msg.button(QMessageBox.Yes)
            buttonY.setText('Ja')
            buttonN = msg.button(QMessageBox.No)
            buttonN.setText('Nein')
            buttonC = msg.button(QMessageBox.Cancel)
            buttonC.setText('Abbrechen')
            msg.setDefaultButton(buttonC)  # Wenn Enter gedrückt wird, wird ButtonC gewählt
            x = msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    print("go")
    sys.exit(app.exec_())
