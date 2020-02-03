import os, sys, random

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from gui.nodeEdit import Ui_nodeEdit
from gui.startWindow import Ui_MainWindow
from gui.mainWidget import Ui_mainWidget
from gui.wizard_1 import Ui_wizard_1
from gui.wizard_2 import Ui_wizard_2
from gui.wizard_3 import Ui_wizard_3
from gui.wizard_4 import Ui_wizard_4
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from node import Node


class MainWindow(QMainWindow):
    switch_window = QtCore.pyqtSignal(
        str)  # Signal wird gesendet, wenn Fenster geändert werden soll: Trägt pdf Pfad mit sich

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.nodeEdit = NodeEdit()  # Erzeugt einen Knoteneditor
        self.__connect_buttons()
        self.startFrame = self.ui.startFrame
        self.last_width = self.width()  #Wird für resizing der Nodes gebraucht
        self.last_height = self.height()

    def __connect_buttons(self):
        self.ui.btnNew.clicked.connect(self.newProject)
        self.ui.btnOpen.clicked.connect(self.openProject)
        self.ui.actionNew.triggered.connect(self.newProject)
        self.ui.actionOpen.triggered.connect(self.openProject)
        self.ui.actionClose.triggered.connect(lambda: self.showPopup("saveBeforeExit"))
        self.ui.actionSave.triggered.connect(lambda: self.showPopup("save"))
        self.ui.actionKnoteneditor.triggered.connect(self.showNodeEdit)

    def showNodeEdit(self): #Wird aufgerufen, wenn der Knoteneditor geöffnet werden soll
        self.ui.actionAlle_Knoten_zeigen.setChecked(True)
        self.nodeEdit.show()
        self.nodeEdit.widget.toggleRects()
        self.nodeEdit.onBtn1()

    def closeEvent(self, event):  # Überschreibt was passiert, wenn das Fenster geschlossen wird
        self.showPopup("saveBeforeExit")  # Fragt, ob gespeichert werden soll
        self.nodeEdit.close()


    def openProject(self):  # Fragt nach einer PDF Datei zum öffnen und speicher den Pfad in path
        Tk().withdraw()  # nur ein Fenster wird geöffnet
        path = askopenfilename(initialdir="../", title="RI - Fließbild wählen",
                               filetypes=(("PNG", "*.png"), ("Alle Dateien", "*.*")))
        if path:
            self.ui.actionAlle_Knoten_zeigen.setEnabled(True)
            self.ui.actionKnoteneditor.setEnabled(True)
            self.ui.actionSave.setEnabled(True)
            self.switch_window.emit(path)

    def resizeEvent(self, event):
        try:
            self.nodeEdit.widget.ui.RILabel.setGeometry(QtCore.QRect(-2, -2, self.frameGeometry().width() - 20,
                                                                     self.frameGeometry().height() - 100))  # Passt das Fließbild an die Fenstergröße an
            for node in self.nodeEdit.widget.nodeList:
                node.resize(self.nodeEdit.widget.width()/self.last_width, self.nodeEdit.widget.height()/self.last_height)
                k = 0
                for i in node.btnList:
                    self.nodeEdit.widget.rectBtnList[i].resize(node.rect[k].width(), node.rect[k].height())  # passe die Buttongröße auf Rechtecksgröße an
                    self.nodeEdit.widget.rectBtnList[i].move(node.rect[k].getCoords()[0],
                                            node.rect[k].getCoords()[1])  # Bewege Button auf die Stelle des Rechtecks
                    k = k + 1
        except AttributeError:
            pass

        QMainWindow.resizeEvent(self, event)

        try:
            self.last_height = self.nodeEdit.widget.height()
            self.last_width = self.nodeEdit.widget.width()
        except AttributeError:
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
            path = askopenfilename(initialdir="../Hazops", title="RI - Fließschema wählen",
                                   filetypes=(("PNG Dateien", "*.png"), ("Alle Dateien", "*.*")))
            self.switch_window.emit(path)
            self.ui.actionAlle_Knoten_zeigen.setEnabled(True)
            self.ui.actionKnoteneditor.setEnabled(True)
            self.ui.actionSave.setEnabled(True)

            # TODO Dateihirarchie ausdenken
        # try:
        #     os.makedirs("../Hazops/Project_X")
        #
        # except FileExistsError:
        #     self.showPopup("folderExists")

    def showPopup(self, info):
        msg = QMessageBox()
        icon = QtGui.QIcon()  # Zeige Logo oben links
        icon.addPixmap(QtGui.QPixmap("../icons/HAZOP.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)  # Zeige Logo oben links
        msg.setWindowIcon(icon)  # Zeige Logo oben links
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
            buttonY.clicked.connect(lambda: QFileDialog.getSaveFileName(self, "Speichern unter"))
            buttonN = msg.button(QMessageBox.No)
            buttonN.setText('Nein')
            buttonC = msg.button(QMessageBox.Cancel)
            buttonC.setText('Abbrechen')
            msg.setDefaultButton(buttonY)  # Wenn Enter gedrückt wird, wird ButtonC gewählt
            x = msg.exec_()
        if info == "deleteNodes":
            msg.setWindowTitle("Knoten löschen")
            msg.setText("Möchten Sie alle zu diesem Knoten gehörigen Elemente entfernen?")
            msg.setIcon(QMessageBox.Question)  # Fragezeichenlogo
            msg.setStandardButtons(
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # Yes/No/ Cancel- Buttons sollen erscheinen
            buttonY = msg.button(QMessageBox.Yes)
            buttonY.setText('Ja')
            buttonN = msg.button(QMessageBox.No)
            buttonN.setText('Nein, nur dieses Element')
            buttonC = msg.button(QMessageBox.Cancel)
            buttonC.setText('Abbrechen')
            msg.setDefaultButton(buttonY)  # Wenn Enter gedrückt wird, wird ButtonC gewählt
            x = msg.exec_()
        if info == "wizardDone":
            msg.setWindowTitle("Hazop Creator")
            msg.setText("Dieser Knoten wurde bereits bearbeitet. Möchten Sie ihn erneut bearbeiten?")
            msg.setIcon(QMessageBox.Question)  # Fragezeichenlogo
            msg.setStandardButtons(
                QMessageBox.Yes | QMessageBox.Cancel)  # Yes/Cancel- Buttons sollen erscheinen
            buttonY = msg.button(QMessageBox.Yes)
            buttonY.setText('Ja')
            buttonC = msg.button(QMessageBox.Cancel)
            buttonC.setText('Abbrechen')
            msg.setDefaultButton(buttonY)  # Wenn Enter gedrückt wird, wird ButtonC gewählt
            x = msg.exec_()



class PushButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        QtWidgets.QPushButton.__init__(self, *args, **kwargs)

    def passWins(self, nod, wi):
        self.node = nod
        self.win = wi

    def enterEvent(self, event):
        if not self.win.ui.actionAlle_Knoten_zeigen.isChecked():
            self.node.show = True
        self.win.nodeEdit.widget.update()

    def leaveEvent(self, event):
        if not self.win.ui.actionAlle_Knoten_zeigen.isChecked():
            self.node.show = False
        self.win.nodeEdit.widget.update()


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
    enableDrawNebennode = False  # Flag zum Malen von Nebenknoten


    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = Ui_mainWidget()
        self.ui.setupUi(self)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

    def passMainWindow(self,
                       win):  # Funktioniert wird von Controller aufgerufen, damit das mainWidget dast startWindow hat
        self.win = win

    def paintEvent(self,
                   event):
        qp = QtGui.QPainter(self)
        for node in self.nodeList:  # Malt alle Rechtecke aus den Knoten aus der Liste
            if node.show or node.painting:
                qp.setBrush(
                    QtGui.QColor(node.rectColor[0], node.rectColor[1], node.rectColor[2],
                                 100))  # Setzt die Farbe des Rechtecks aus der rectColor Liste des Knotens
                for rect in node.rect:
                    if rect.x() >= 0:  # Rechtecke nur malen, wenn sie nicht verkleinert sind
                        qp.drawRect(rect)  # Malt Rechtecke


    def mousePressEvent(self, event):
        if self.enableDrawNode:
            self.begin = event.pos()
            self.end = event.pos()
            # Neuen Knoten erstellen
            self.nodeList.append(Node())
        elif self.enableDrawNebennode:
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
            try:
                self.nodeList[self.nodei].rect[self.recti] = QtCore.QRect(self.begin,
                                                                      self.end)  # Updatet die Rechtecke in der RectListe
            except IndexError:
                pass
        self.update()

    def mouseReleaseEvent(self, event):
        if self.enableDrawNode or self.enableDrawNebennode:
            self.recti = self.recti + 1
            self.win.nodeEdit.rectSignal.emit()  # schickt ein Signal an den NodeEdit
        if self.enableDeleteNode:
            self.win.nodeEdit.onBtnBin()
            self.win.nodeEdit.ui.btnOk.setEnabled(True)
            for node in self.nodeList[::-1]:  # Geht alle  Nodes durch
                for rect in node.rect:  # Geht alle Rechtecke durch um zu prüfen, welches gelöscht werden soll
                    if rect.contains(event.pos()):
                        if len(node.rect) > 1:
                            self.win.showPopup("deleteNodes")
                        node.hideRects()
                        for g in node.btnList:
                            self.rectBtnList[g].setGeometry(0, 0, 0, 0)
                            self.rectBtnList[g].hide()
                        break
                else:
                    continue
                break
        self.update()

    def createRectBtn(self, node):
        for rect in node.rect:
            self.rectBtnList.append(PushButton(self))  # erstelle neuen Button
            i = len(self.rectBtnList) - 1
            self.rectBtnList[i].passWins(node, self.win)
            self.rectBtnList[i].resize(rect.width(), rect.height())  # passe die Buttongröße auf Rechtecksgröße an
            self.rectBtnList[i].move(rect.getCoords()[0],
                                     rect.getCoords()[1])  # Bewege Button auf die Stelle des Rechtecks
            self.rectBtnList[i].setObjectName("btn1")
            self.rectBtnList[i].setVisible(True)
            self.rectBtnList[i].setFlat(True)  # Macht den Button durchsichtig
            nodek = self.nodei
            self.rectBtnList[i].clicked.connect(lambda: self.openWizard(nodek))
            self.rectBtnList[i].show()
            self.rectBtnList[
                i].setEnabled(False)  # Btn erstmal hiden und erst wenn Ok gedrückt wird shown, sonst crasht das Programm beim Malen
            node.setIndizes(i)
            node.painting = False

    def toggleRects(self):  # Wird aufgerufen, wenn bei Rechteckezeigen ein Häkchen verändert wird
        if self.win.ui.actionAlle_Knoten_zeigen.isChecked():
            for node in self.nodeList:
                node.show = True
        else:
            for node in self.nodeList:
                node.show = False
        self.repaint()

    def openWizard(self, i):
        if self.nodeList[i].done == False:
            self.win.switch_window.emit(str(i))
        else:
            self.win.showPopup("wizardDone")
            self.win.switch_window.emit(str(i))

# ---------------------------------------------------------------- #
#                         Node-Editor
# ---------------------------------------------------------------- #

class NodeEdit(QMainWindow):
    rectSignal = QtCore.pyqtSignal()  # Signal wird von gesendet, wenn ein Rechteck erstellt wurde
    rectPos = QtCore.QRect(0, 0, 0, 0)

    def __init__(self):
        QMainWindow.__init__(self, None,
                             QtCore.Qt.WindowStaysOnTopHint)  # Lässt den Knoteneditor immer im Vordergrund stehen
        self.ui = Ui_nodeEdit()
        self.ui.setupUi(self)
        self.rectSignal.connect(self.onRectCreate)
        self.__connect_buttons()
        self.rectPos = QtCore.QRect(19, 19, 42, 42)  # Hauptknoten erstellen
        icon = QtGui.QIcon()  # Zeige Logo oben links
        icon.addPixmap(QtGui.QPixmap("../icons/HAZOP.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)  # Zeige Logo oben links
        self.setWindowIcon(icon)  # Zeige Logo oben links

    def paintEvent(self, event):
        rectColor = QtGui.QColor(28, 134, 238, 200)
        qp = QtGui.QPainter(self)
        qp.setBrush(rectColor)  # Setzt die Farbe des Rechtecks aus den RGB Listen
        qp.drawRect(self.rectPos)  # Malt Rechteck

    def __connect_buttons(self):  # Legt fest welche Funktionen mit welchem Button verknüpft sind
        self.ui.btn1.clicked.connect(self.onBtn1)
        self.ui.btn2.clicked.connect(self.onBtn2)
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
        self.ui.btnBin.setEnabled(True) # Löschbutton bleibt aktiv
        for btn in self.widget.rectBtnList:  # Alle Buttons während dem Malen disablen, damit das Programm nicht crasht
            btn.setEnabled(False)

    def onBtn2(self):
        self.rectPos = QtCore .QRect(69, 74, 42, 42)
        self.update()
        pass

    def onBtnBin(self):
        self.ui.btnOk.setEnabled(False)
        self.ui.btn2.setEnabled(False)
        self.rectPos = QtCore.QRect(19, 159, 42, 42)
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
        self.ui.btnBin.setEnabled(True)
        self.ui.btnOk.setEnabled(False)
        for btn in self.widget.rectBtnList:  # Schaltet jetzt erst die Buttons an, damit die beim Malen nicht geklickt werden
            btn.setEnabled(True)
        self.widget.recti = 0
        self.widget.repaint()
        self.widget.win.ui.actionExportieren_als_Tabelle.setEnabled(True)


    def onBtnAbort(self):
        self.rectPos = QtCore.QRect(0, 0, 0, 0)  # Markierungsrechteck wird verschoben
        self.update()
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
            self.ui.btnOk.setEnabled(True)
        else:
            self.ui.btn2.setEnabled(False)  # Buttons disablen, wenn es keine Rechtecke gibt
            self.ui.btnOk.setEnabled(False)
            self.ui.btnBin.setEnabled(True)


# ---------------------------------------------------------------- #
#                         Wizards
# ---------------------------------------------------------------- #
class Wizard_1(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None,
                             QtCore.Qt.WindowStaysOnTopHint)  # Lässt den Wizard immer im Vordergrund stehen
        self.ui = Ui_wizard_1()
        self.ui.setupUi(self)
        self.ui.weiterButton.clicked.connect(lambda: self.openNextWizard(""))

    def openNextWizard(self, i):
        self.con.showWizard_2(i)

    def passController(self, controll):
        self.con = controll


class Wizard_2(QtWidgets.QWidget):
    def __init__(self):
        super(Wizard_2, self).__init__()
        self.ui = Ui_wizard_2()
        self.ui.setupUi(self)
        self.ui.weiterButton.clicked.connect(lambda: self.openNextWizard(""))
        self.ui.zuruckButton.clicked.connect(lambda: self.openPreviousWizard((self.con.i)))

    def openNextWizard(self, i):
        self.con.showWizard_3(i)

    def openPreviousWizard(self, i):
        self.con.showWizard(i)

    def passController(self, controll):
        self.con = controll


class Wizard_3(QtWidgets.QWidget):
    def __init__(self):
        super(Wizard_3, self).__init__()
        self.ui = Ui_wizard_3()
        self.ui.setupUi(self)
        self.ui.weiterButton.clicked.connect(lambda: self.openNextWizard(""))
        self.ui.zuruckButton.clicked.connect(lambda: self.openPreviousWizard(("")))

    def openNextWizard(self, i):
        self.con.showWizard_4(i)

    def passController(self, controll):
        self.con = controll

    def openPreviousWizard(self, i):
        self.con.showWizard_2(i)


class Wizard_4(QtWidgets.QWidget):
    def __init__(self):
        super(Wizard_4, self).__init__()
        self.ui = Ui_wizard_4()
        self.ui.setupUi(self)
        self.ui.weiterButton.clicked.connect(lambda: self.openNextWizard(""))
        self.ui.zuruckButton.clicked.connect(lambda: self.openPreviousWizard(("")))

    def openPreviousWizard(self, i):
        self.con.showWizard_3(i)

    def openNextWizard(self, i):
        self.con.mainWidget.nodeList[int(self.con.i)].done = True     #Der Knoten ist nun fertig bearbeitet und beim erneuten Öffnen wird das gemeldet

    def passController(self, controll):
        self.con = controll


# ---------------------------------------------------------------- #
#                         Controller
# ---------------------------------------------------------------- #
class Controller:  # Verwaltet die verschiedenen Widgets
    def __init__(self):
        self.i = 0  #Knoten ID, welcher gerade im Wizard bearbeitet wird

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
        self.startWindow.switch_window.disconnect()
        self.startWindow.switch_window.connect(self.showWizard)
        self.mainWidget.enableDrawNode = True
        self.startWindow.ui.actionAlle_Knoten_zeigen.triggered.connect(self.mainWidget.toggleRects)
        self.startWindow.ui.actionExportieren_als_Tabelle.triggered.connect(lambda: self.openExcel())

    def openExcel(self):
        os.startfile('pHAZOP-Gesamt.xlsx')
        self.startWindow.nodeEdit.hide()

    def showWizard(self, i):
        self.i = i
        self.wizard = Wizard_1()
        self.wizard.passController(self)
        self.wizard.setWindowTitle("Hazop Assistent | Knoten-ID: "+str(self.i))
        self.wizard.show()
        self.startWindow.nodeEdit.hide()
        self.wizard.setCentralWidget(self.wizard.ui.frame)

    def showWizard_2(self, i):
        self.wizard2 = Wizard_2()
        self.wizard2.passController(self)
        self.wizard.setCentralWidget(self.wizard2)

    def showWizard_3(self, i):
        self.wizard3 = Wizard_3()
        self.wizard3.passController(self)
        self.wizard.setCentralWidget(self.wizard3)

    def showWizard_4(self, i):
        self.wizard4 = Wizard_4()
        self.wizard4.passController(self)
        self.wizard.setCentralWidget(self.wizard4)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showStart()
    sys.exit(app.exec_())