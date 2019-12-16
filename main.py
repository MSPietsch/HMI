from gui.test import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__connect_buttons()

    def __connect_buttons(self):
        self.ui.btn1.clicked.connect(self.fkt)
        self.ui.actionTest.triggered.connect(lambda: print("TEST JA"))

    def fkt(self):
        self.ui.label1.setText("Hallo ich bin Malte")
        print("Test!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    print("go")
    sys.exit(app.exec_())