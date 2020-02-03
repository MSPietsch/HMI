from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Node():
    # Jeder Knoten hat Listen mit Rechtecken und einer Farbe
    
    def __init__(self):
        self.btnList = []   #hier kommen die Indizes der Buttons in der btnList des mainWidgets herein, die zu diesem Knoten gehören
        self.rect = []
        self.rect.append(QtCore.QRect(0, 0, 0, 0))
        self.rectColor = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.show = True    #Versteckt oder sichtbar (mouseover feature)
        self.done = False
        self.painting = True    #Flag um zu zeigen, dass der knoten zu Ende gemalt wurde (mouseover feature) damit er auch gezeigt wird, auch wenn alle auf mouseover sind

    def hideRects(self):
        for rec in self.rect:
            rec.setCoords(-1, 0, 0, 0)

    def addRect(self, recti):
        if recti == len(self.rect):
            self.rect.append(QtCore.QRect(0, 0, 0, 0))

    def setIndizes(self, i):
        self.btnList.append(i)

    def resize(self, scale_w, scale_h): #Scaling Factor ist noch nicht richtig, aber genügt erstmal
        for rect in self.rect:
            rect.adjust(rect.x()*(scale_w-1), rect.y() * (scale_h - 1), rect.right()*(scale_w - 1), rect.bottom() * (scale_h - 1))