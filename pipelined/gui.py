#! /usr/bin/env python
#
# virtualenv -p python3.5 virtualenv
# . ./virtualenv/bin/activate
# pip3 install PyQt5


import sys
from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtCore import (QEasingCurve, QFileInfo, QLineF, QMimeData,
        QParallelAnimationGroup, QPoint, QPointF, QPropertyAnimation, qrand,
        QRectF, qsrand, Qt, QTime)
from PyQt5.QtGui import (QBrush, QColor, QDrag, QImage, QPainter, QPen,
        QPixmap, QTransform, QPolygonF)
from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsObject,
        QGraphicsScene, QGraphicsView)

import generic

class Mux(QGraphicsItem):
    def __init__(self):
        super().__init__()

        self.color = QColor(0, 0, 255)
        self._width = 10

        self.setIncoming(0)

    def setIncoming(self, incoming):
        self.incoming = incoming
        self._height = 20 + self.incoming * 10

    def boundingRect(self):
        return QRectF(0, 0, self._width, self._height)

    def paint(self, painter, option, widget):
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush(self.color))
        painter.drawPolygon(QPolygonF([QPointF(0,0), QPointF(self._width,10), QPointF(self._width, self._height - 10), QPointF(0,self._height)]))

class ALU(QGraphicsItem):
    def __init__(self):
        super().__init__()

        self.color = QColor(150, 150, 150)

    def boundingRect(self):
        return QRectF(0, 0, 10, 30)

    def paint(self, painter, option, widget):
        pen = QPen(Qt.black, 2)
        pen.setCosmetic(True)
        painter.setPen(pen)
        painter.setBrush(QBrush(self.color))
        painter.drawPolygon(QPolygonF([QPointF(0,0),
                                       QPointF(10,10),
                                       QPointF(10,20),
                                       QPointF(0,30),
                                       QPointF(0,20),
                                       QPointF(3.5,15),
                                       QPointF(0,10)]))
viewMap = {
  generic.abstractcomponents.Mux: Mux,
  generic.ALU.ALU: ALU
}

def mapModelsToViews(models):
  modelsToViews = {}
  for m in models:
    modelsToViews[m] = viewMap[m.__class__]()

  return modelsToViews

def GUI():
    app = QApplication(sys.argv)

    scene = QGraphicsScene(-50, -50, 400, 400)

    mux_s1 = Mux()
    mux_s1.setIncoming(4)
    mux_s1.setPos(0, 0)
    scene.addItem(mux_s1)

    mux_s2 = Mux()
    mux_s2.setIncoming(4)
    mux_s2.setPos(0, mux_s2._height + 20)
    scene.addItem(mux_s2)

    alu = ALU()
    alu.setPos(mux_s2.pos() + QPointF(mux_s2._width + 40, 0))
    alu.setScale(4)
    scene.addItem(alu)

    view = QGraphicsView(scene)
    view.setRenderHint(QPainter.Antialiasing)
    view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
    view.scale(2, 2)
    view.setBackgroundBrush(QColor(230, 200, 167))
    view.setWindowTitle("Pipelined Microarchitecture")
    view.show()

    
    sys.exit(app.exec_())
