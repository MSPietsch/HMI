import os, sys, random

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from gui.nodeEdit import Ui_nodeEdit
from gui.startWindow import Ui_MainWindow
from gui.mainWidget import Ui_mainWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from node import Node


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


# ---------------------------------------------------------------- #
#                        Hauptfenster
# ---------------------------------------------------------------- #
class MainWidget(QtWidgets.QWidget):
    nodeList = []  # Hier kommen alle Nodes rein
    rectBtnList = []  # Liste mit allen Buttons
    recti = 0  # Variable für Anzahl der Rechtecke innerhalb des derzeitigen Knotens
    nodei = 0  # Variable für tatsächliche Knoten Haupt und Nebenknoten haben die gleiche Zahl
    enableDrawNode = False  # Vorerst können keine Rechtecke gemalt werden
    enableDeleteNode = False  # Flag zum Löschen von Knoten
    enableDrawNebennode =  False #Flag zum Malen von Nebenknoten

    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = Ui_mainWidget()
        self.ui.setupUi(self)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

    def passMainWindow(self,
                       win):  # Funktioniert wird von Controller aufgerufen, damit das mainWidget dast startWindow hat
        self.win = win

    def paintEvent(self, event): #TODO: Wenn der Haken bei Alle Knoten anzeigen raus ist, dann sollen die Rechtecke trotzdem bei Mouseover sichtbar
        qp = QtGui.QPainter(self)
        # br = QtGui.QBrush(QtGui.QColor(r, g, b, 100))
        for node in self.nodeList:  # Malt alle Rechtecke aus den Knoten aus der Liste
            qp.setBrush(
                QtGui.QColor(node.rectColor[0], node.rectColor[1], node.rectColor[2], 100))  # Setzt die Farbe des Rechtecks aus der rectColor Liste des Knotens
            for rect in node.rect:
                if rect.x() >= 0:    #Rechtecke nur malen, wenn sie nicht verkleinert sind
                    qp.drawRect(rect)  # Malt Rechtecke

    def mousePressEvent(self, event):
        if self.enableDrawNode:
            print("Ja")
            self.begin = event.pos()
            self.end = event.pos()
            # Neuen Knoten erstellen
            self.nodeList.append(Node())
        elif self.enableDrawNebennode:
            print("neben")
            self.begin = event.pos()
            self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        if self.enableDrawNode:
            self.end = event.pos()
            self.nodeList[self.nodei].rect[self.recti] = QtCore.QRect(self.begin,
                                                                      self.end)  # Updatet die Rechtecke in der RectListe
        elif self.enableDrawNebennode:
            self.end = event.pos()
            self.nodeList[self.nodei].addRect(self.recti)
            self.nodeList[self.nodei].rect[self.recti] = QtCore.QRect(self.begin,
                                                                      self.end)  # Updatet die Rechtecke in der RectListe
        self.update()

    def mouseReleaseEvent(self, event):
        if self.enableDrawNode or self.enableDrawNebennode:
            self.recti = self.recti + 1
            self.win.nodeEdit.rectSignal.emit()  # schickt ein Signal an den NodeEdit
        if self.enableDeleteNode:
            for node in self.nodeList[::-1]:  # Geht alle  Nodes durch
                for rect in node.rect:  # Geht alle Rechtecke durch um zu prüfen, welches gelöscht werden soll
                    if rect.contains(event.pos()):
                        node.hideRects()
                        for g in node.btnList:
                            self.rectBtnList[g].setGeometry(0, 0, 0, 0)
                            self.rectBtnList[g].setEnabled(False)
                        break
                else:
                    continue
                break
        self.update()

    def createRectBtn(self, node):
        for rect in node.rect:
            self.rectBtnList.append(QtWidgets.QPushButton(self))  # erstelle neuen Button
            i = len(self.rectBtnList) - 1
            self.rectBtnList[i].resize(rect.width(), rect.height())  # passe die Buttongröße auf Rechtecksgröße an
            self.rectBtnList[i].move(rect.getCoords()[0],
                                     rect.getCoords()[1])  # Bewege Button auf die Stelle des Rechtecks
            self.rectBtnList[i].setObjectName("btn1")
            self.rectBtnList[i].setVisible(True)
            self.rectBtnList[i].setFlat(True)  # Macht den Button durchsichtig
            nodek = self.nodei
            self.rectBtnList[i].clicked.connect(lambda: self.openWizard(nodek))
            self.rectBtnList[
                i].hide()  # Btn erstmal hiden und erst wenn Ok gedrückt wird shown, sonst crasht das Programm beim Malen
            node.setIndizes(i)

    def openWizard(self, i):
        print(i)


# ---------------------------------------------------------------- #
#                         Node-Editor
# ---------------------------------------------------------------- #

class NodeEdit(QMainWindow):
    rectSignal = QtCore.pyqtSignal()  # Signal wird von gesendet, wenn ein Rechteck erstellt wurde
    rectPos = QtCore.QRect(0, 0, 0, 0)

    def paintEvent(self, event):
        rectColor = QtGui.QColor(28, 134, 238, 200)
        qp = QtGui.QPainter(self)
        qp.setBrush(rectColor)  # Setzt die Farbe des Rechtecks aus den RGB Listen
        qp.drawRect(self.rectPos)  # Malt Rechteck

    def __init__(self):
        QMainWindow.__init__(self, None,
                             QtCore.Qt.WindowStaysOnTopHint)  # Lässt den Knoteneditor immer im Vordergrund stehen
        self.ui = Ui_nodeEdit()
        self.ui.setupUi(self)
        self.rectSignal.connect(self.onRectCreate)
        self.__connect_buttons()
        self.rectPos = QtCore.QRect(19, 19, 42, 42) #Hauptknoten erstellen

    def __connect_buttons(self):  # Legt fest welche Funktionen mit welchem Button verknüpft sind
        self.ui.btn1.clicked.connect(self.onBtn1)
        self.ui.btn2.clicked.connect(self.onBtn2)
        self.ui.btn3.clicked.connect(self.onBtn3)
        self.ui.btnOk.clicked.connect(self.onBtnOk)
        self.ui.btnBin.clicked.connect(self.onBtnBin)
        self.ui.btnAbort.clicked.connect(self.onBtnAbort)

    # Funktionen für die Buttons des Knoteneditors
    def onBtn1(self):
        self.rectPos = QtCore.QRect(19, 19, 42, 42)
        self.update()
        self.widget.enableDrawNode = True
        self.widget.enableDrawNebennode = False
        self.widget.enableDeleteNode = False
        self.ui.btnBin.setEnabled(False)
        for btn in self.widget.rectBtnList:  # Alle Buttons während dem Malen disablen, damit das Programm nicht crasht
            btn.hide()

    def onBtn2(self):
        print("2")
        self.rectPos = QtCore.QRect(69, 74, 42, 42)
        self.update()
        pass

    def onBtn3(self):       #TODO: Referenzpunkt soll doch nicht drin sein, sonder siehe todo bei paintEvent
        print("3")
        self.rectPos = QtCore.QRect(19, 129, 42, 42)
        self.update()
        pass

    def onBtnBin(self):
        self.ui.btnOk.setEnabled(False)
        self.ui.btn2.setEnabled(False)
        self.ui.btn3.setEnabled(False)
        self.ui.btnOk.setEnabled(False)
        self.rectPos = QtCore.QRect(19, 199, 42, 42)
        self.update()
        self.widget.enableDrawNode = False
        self.widget.enableDrawNebenode = False
        self.widget.enableDeleteNode = True
        for btn in self.widget.rectBtnList:  # Alle Buttons disablen, damit die Buttons nicht gedrückt werden
            btn.hide()

    def onBtnOk(self):
        self.widget.createRectBtn(self.widget.nodeList[self.widget.nodei])
        self.widget.nodei = self.widget.nodei + 1  # Knoten abschließen und einen neuen Knoten eröffnen
        self.rectPos = QtCore.QRect(0, 0, 0, 0)  # Markierungsrechteck wird verschoben
        self.update()
        self.widget.enableDrawNode = False
        self.widget.enableDrawNebennode = False
        self.widget.enableDeleteNode = False
        self.ui.btnOk.setEnabled(False)
        self.ui.btn1.setEnabled(True)
        self.ui.btn2.setEnabled(False)
        self.ui.btn3.setEnabled(False)
        self.ui.btnBin.setEnabled(True)
        self.ui.btnOk.setEnabled(False)
        for btn in self.widget.rectBtnList:  # Schaltet jetzt erst die Buttons an, damit die beim Malen nicht geklickt werden -> Crash
            btn.show()
        self.widget.recti = 0

    def onBtnAbort(self):
        self.rectPos = QtCore.QRect(0, 0, 0, 0)  # Markierungsrechteck wird verschoben
        self.update()
        print("Abbruch")
        self.hide()

    def passWidget(self, widget):
        self.widget = widget

    def onRectCreate(self):  # Funktion wird aufgerufen, wenn in mainWidget ein Rechteck erstellt wurde
        self.ui.btn1.setEnabled(False)  # Disablen, damit nur ein Knoten erstmal gezeichnet wird
        self.widget.enableDrawNode = False
        self.widget.enableDrawNebennode = True
        self.rectPos = QtCore.QRect(69, 74, 42, 42)
        self.repaint()
        if self.widget.recti > 0:  # Wenn es mindestens ein Rechteck existiert
            self.ui.btn2.setEnabled(True)  # Buttons enablen
            self.ui.btn3.setEnabled(True)
            self.ui.btnOk.setEnabled(True)
        else:
            self.ui.btn2.setEnabled(False)  # Buttons disablen, wenn es keine Rechtecke gibt
            self.ui.btn3.setEnabled(False)
            self.ui.btnOk.setEnabled(False)
            self.ui.btnBin.setEnabled(False)


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
        self.startWindow.ui.actionAlle_Knoten_zeigen.setChecked(True)
        self.startWindow.nodeEdit.passWidget(self.mainWidget)  # Übergibt das mainWidget an den nodeEdit
        self.startWindow.startFrame.hide()  # Startframe verbergen
        self.startWindow.setCentralWidget(self.mainWidget)  # Labelansicht ins Fenster stecken
        self.mainWidget.ui.RILabel.setPixmap(QtGui.QPixmap(path))  # Bilddatei wird im Label angezeigt
        self.startWindow.nodeEdit.show()
        self.startWindow.nodeEdit.move(200, 300)  # Positioniert den Knoteneditor
        self.mainWidget.enableDrawNode = True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showStart()
    sys.exit(app.exec_())
