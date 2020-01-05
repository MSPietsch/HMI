import os, sys, random

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from gui.nodeEdit import Ui_nodeEdit
from gui.startWindow import Ui_MainWindow
from gui.mainWidget import Ui_mainWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox


class MainWindow(QMainWindow):
    switch_window = QtCore.pyqtSignal(
        str)  # Signal wird gesendet, wenn Fenster geändert werden soll: Trägt pdf Pfad mit sich

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__connect_buttons()
        self.startFrame = self.ui.startFrame
        self.nodeEdit = NodeEdit()  # Erzeugt einen Knoteneditor

    def __connect_buttons(self):
        self.ui.btnNew.clicked.connect(self.newProject)
        self.ui.btnOpen.clicked.connect(self.openProject)
        self.ui.actionNew.triggered.connect(self.newProject)
        self.ui.actionOpen.triggered.connect(self.openProject)
        self.ui.actionClose.triggered.connect(lambda: self.showPopup("saveBeforeExit"))
        self.ui.actionSave.triggered.connect(lambda: self.showPopup("save"))

    def closeEvent(self, event):  # Überschreibt was passiert, wenn das Fenster geschlossen wird
        self.showPopup("saveBeforeExit")  # Fragt, ob gespeichert werden soll
        self.nodeEdit.close()  # Schließt auch den Knoteneditor, auch wenn er versteckt ist

    def openProject(self):  # Fragt nach einer PDF Datei zum öffnen und speicher den Pfad in path
        Tk().withdraw()  # nur ein Fenster wird geöffnet
        path = askopenfilename(initialdir="../", title="RI - Fließbild wählen",
                               filetypes=(("PNG", "*.png"), ("Alle Dateien", "*.*")))
        if path:
            self.ui.actionAlle_Knoten_zeigen.setEnabled(True)
            self.ui.actionSave.setEnabled(True)
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
            self.ui.actionAlle_Knoten_zeigen.setEnabled(True)
            self.ui.actionSave.setEnabled(True)

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
        if info == "saveBeforeExit":  # Hier sollte noch definiert werden was die Buttons tun
            # https://stackoverflow.com/questions/40622095/pyqt5-closeevent-method ALS BEISPIEl
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
    rectList = [QtCore.QRect(0, 0, 0, 0)]  # Hier kommen alle Rechtecke rein, die gemalt werden sollen
    rectBtnList = []    #Liste mit allen Buttons
    recti = 0
    enableDrawNode = False  #Vorerst können keine Rechtecke gemalt werden
    enableDeleteNode = False  #Flag zum Löschen von Knoten

    r = [random.randint(0, 255)]  # Listen mit dem Rotwert der Rechtecke wird erstellt, mit erstem Wert
    g = [random.randint(0, 255)]  # Listen mit dem Gelbwert der Rechtecke wird erstellt, mit erstem Wert
    b = [random.randint(0, 255)]  # Listen mit dem Blauwert der Rechtecke wird erstellt, mit erstem Wert

    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = Ui_mainWidget()
        self.ui.setupUi(self)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

    def passMainWindow(self,
                       win):  # Funktioniert wird von Controller aufgerufen, damit das mainWidget dast startWindow hat
        self.win = win

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        # br = QtGui.QBrush(QtGui.QColor(r, g, b, 100))
        i = 0
        for rect in self.rectList:  # Malt alle Rechtecke aus der Liste
            rectColor = QtGui.QColor(self.r[i], self.g[i], self.b[i], 100)
            qp.setBrush(rectColor)  # Setzt die Farbe des Rechtecks aus den RGB Listen
            qp.drawRect(rect)  # Malt Rechteck
            i = i + 1  # Laufvariable für RGB Listen erhöht

    def mousePressEvent(self, event):
        if self.enableDrawNode:
            print("Ja")
            self.begin = event.pos()
            self.end = event.pos()
            self.r.insert(self.recti + 1, random.randint(0, 255))  # Neue Farbe für Rechteck erstellen
            self.g.insert(self.recti + 1, random.randint(0, 255))
            self.b.insert(self.recti + 1, random.randint(0, 255))
        self.update()

    def mouseMoveEvent(self, event):
        if self.enableDrawNode:
            self.end = event.pos()
            self.rectList[self.recti] = QtCore.QRect(self.begin, self.end)  # Updatet die Rechtecke in der RectListe
        self.update()

    def mouseReleaseEvent(self, event):
        self.createRectBtn(self.rectList[self.recti])
        self.recti = self.recti + 1
        self.rectList.append(QtCore.QRect(0, 0, 0, 0))
        self.update()

    def createRectBtn(self, rect):
        self.btn1 = QtWidgets.QPushButton(self)  # erstelle Button
        self.btn1.resize(rect.width(), rect.height())  # passe die Buttongröße auf Rechtecksgröße an
        self.btn1.move(rect.getCoords()[0], rect.getCoords()[1])  # Bewege Button auf die Stelle des Rechtecks
        self.btn1.setObjectName("btn1")
        self.btn1.show()
        self.btn1.setVisible(True)

    def openWizard(self, i):
        print(i)

class NodeEdit(QMainWindow):
    rectSignal = QtCore.pyqtSignal()  # Signal wird von gesendet, wenn ein Rechteck erstellt wurde

    def __init__(self):
        QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)    #Lässt den Knoteneditor immer im Vordergrund stehen
        self.ui = Ui_nodeEdit()
        self.ui.setupUi(self)
        self.rectSignal.connect(self.onRectCreate)
        self.__connect_buttons()

    def __connect_buttons(self):  # Legt fest welche Funktionen mit welchem Button verknüpft sind
        self.ui.btn1.clicked.connect(self.onBtn1)
        self.ui.btn2.clicked.connect(self.onBtn2)
        self.ui.btn3.clicked.connect(self.onBtn3)
        self.ui.btnOk.clicked.connect(self.onBtnOk)
        self.ui.btnBin.clicked.connect(self.onBtnBin)
        self.ui.btnAbort.clicked.connect(self.onBtnAbort)

    # Funktionen für die Buttons des Knoteneditors
    def onBtn1(self):
        self.widget.enableDrawNode = True
        self.widget.enableDeleteNode = False
        for btn in self.widget.rectBtnList:         #Alle Buttons während dem Malen disablen, damit das Programm nicht crasht
            btn.hide()

    def onBtn2(self):
        print("2")
        pass

    def onBtn3(self):
        print("3")
        pass

    def onBtnBin(self):
        self.widget.enableDrawNode = False
        self.widget.enableDeleteNode = True

    def onBtnOk(self):
        self.widget.enableDrawNode = False
        self.widget.enableDeleteNode = False
        for btn in self.widget.rectBtnList:         #Schaltet jetzt erst die Buttons an, damit die beim Malen nicht geklickt werden -> Crash
            btn.show()
        print("Ok")
        pass

    def onBtnAbort(self):
        print("Abbruch")
        pass

    def passWidget(self, widget):
        self.widget = widget

    def onRectCreate(self):  # Funktion wird aufgerufen, wenn in mainWidget ein Rechteck erstellt wurde
        if self.widget.recti > 0:  # Wenn es mindestens ein Rechteck existiert
            self.ui.btn2.setEnabled(True)  # Buttons enablen
            self.ui.btn3.setEnabled(True)
            self.ui.btnOk.setEnabled(True)
        else:
            self.ui.btn2.setEnabled(False)  # Buttons disablen, wenn es keine Rechtecke gibt
            self.ui.btn3.setEnabled(False)
            self.ui.btnOk.setEnabled(False)


#  def __connect_buttons(self):
# self.ui.btnMaus1.clicked.connect(self.pass)
# self.ui.btnMaus2.clicked.connect(self.pass)
# self.ui.btnBin.clicked.connect(self.pass)


class Controller:  # Verwaltet die verschiedenen Widgets
    def __init__(self):
        pass

    def showStart(self):
        self.startWindow = MainWindow()
        self.startWindow.switch_window.connect(self.showMain)
        self.startWindow.show()

    def showMain(self, path):
        self.mainWidget = MainWidget()
        self.mainWidget.passMainWindow(self.startWindow)  # Übergibt das Hauptfenster an das mainWidget
        self.startWindow.nodeEdit.passWidget(self.mainWidget)  # Übergibt das mainWidget an den nodeEdit
        self.startWindow.startFrame.hide()  # Startframe verbergen
        self.startWindow.setCentralWidget(self.mainWidget)  # Labelansicht ins Fenster stecken
        self.mainWidget.ui.RILabel.setPixmap(QtGui.QPixmap(path))  # Bilddatei wird im Label angezeigt
        self.startWindow.nodeEdit.show()
        self.startWindow.nodeEdit.move(200, 300)  # Positioniert den Knoteneditor


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showStart()
    sys.exit(app.exec_())
