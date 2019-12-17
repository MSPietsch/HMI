import os, sys

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

from gui.startWindow import Ui_MainWindow
from gui.mainWidget import Ui_mainWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox


##
class MainWindow(QMainWindow):
    switch_window = QtCore.pyqtSignal(str)  # Signal wird gesendet, wenn Fenster geändert werden soll: Kann Parameter versenden

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__connect_buttons()
        self.startFrame = self.ui.startFrame

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
                               filetypes=(("PNG Dateien", "*.png"), ("Alle Dateien", "*.*")))
        print(path)
        self.switch_window.emit(path)

    def newProject(self):
        Tk().withdraw()  # nur ein Fenster wird geöffnet
        directory = askdirectory(
            title="Projektspeicherort auswählen",
            mustexist=1
        )
        if directory:
            # Falls ein Pfad ausgewählt wurde muss ein RI-Fließschema ausgewählt werden
            Tk().withdraw()  # nur ein Fenster wird geöffnet
            path = askopenfilename(initialdir="../Hazops", title="RI - Fließschema wählen",
                                   filetypes=(("PNG Dateien", "*.png"), ("Alle Dateien", "*.*")))
            self.switch_window.emit(path)

            # TODO Dateihirarchie ausdenken
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
        if info == "save":  # TODO: Speicherfunktion einfügen
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

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = Ui_mainWidget()
        self.ui.setupUi(self)
        # self.__connect_buttons()


class Controller:  # Verwaltet die verschiedenen Widgets^

    def __init__(self):
        pass

    def showStart(self):
        self.startWindow = MainWindow()
        self.startWindow.switch_window.connect(self.showMain)
        self.startWindow.show()
        print("startWindow erstellt.")

    def showMain(self, path):
        self.mainWidget = MainWidget()
        self.startWindow.startFrame.hide()
        self.startWindow.setCentralWidget(self.mainWidget)
        self.mainWidget.ui.RILabel.setPixmap(QtGui.QPixmap(path))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showStart()
    print("go")
    sys.exit(app.exec_())
