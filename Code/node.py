from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Node():
    # Jeder Knoten hat Listen mit Rechtecken und einer Farbe
    
    def __init__(self):
        self.btnList = []   #hier kommen die Indizes der Buttons herein, die zu diesem Knoten gehören
        self.rect = []
        self.rect.append(QtCore.QRect(0, 0, 0, 0))
        self.rectColor = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

    def setRect(self, rect):
        self.rect.append(rect)

    def hideRects(self):
        for rec in self.rect:
            rec.setCoords(-1, 0, 0, 0)

    def setIndizes(self, i):
        self.btnList.append(i)