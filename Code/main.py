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
        self.ui.actionClose.triggered.connect(lambda: self.showPopup("saveBeforeExit"))
        self.ui.actionSave.triggered.connect(lambda: self.showPopup("save"))

    def openProject(self):  # Fragt nach einer PDF Datei zum öffnen und speicher den Pfad in path
        Tk().withdraw()  # nur ein Fenster wird geöffnet
        path = askopenfilename(initialdir="../", title="RI - Fließbild wählen",
                               filetypes=(("PDF Dateien", "*.pdf"), ("Alle Dateien", "*.*")))
        print(path)

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

    def showPopup(self, info):
        msg = QMessageBox()
        if info == "folderExists":
            msg.setWindowTitle("Mitteilung")
            msg.setText("Dieser Ordner existiert bereits. Bitte wählen Sie einen anderen Projektnamen.")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        if info == "save":      #TODO: Speicherfunktion einfügen
            msg.setWindowTitle("Mitteilung")
            msg.setText("Platzhalter: Projekt wurde gespeichert!")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
        if info == "saveBeforeExit":
            msg.setWindowTitle("Achtung")
            msg.setText("Möchten Sie Ihr Projekt vor dem Schließen speichern?")
            msg.setIcon(QMessageBox.Question)  # Fragezeichenlogo
            msg.setStandardButtons(
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # Yes/No/ Cancel- Buttons sollen erscheinen
            # Übersetzung der Buttons ins Deutsche
            buttonY = msg.button(QMessageBox.Yes)
            buttonY.setText('Ja')
            buttonN = msg.button(QMessageBox.No)
            buttonN.setText('Nein')
            buttonC = msg.button(QMessageBox.Cancel)
            buttonC.setText('Abbrechen')
            msg.setDefaultButton(buttonY)  # Wenn Enter gedrückt wird, wird ButtonC gewählt
            x = msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    print("go")
    sys.exit(app.exec_())
