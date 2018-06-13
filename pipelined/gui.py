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

class Mux(QGraphicsItem):
    def __init__(self):
        super().__init__()

        self.color = QColor(0, 0, 255)

    def boundingRect(self):
        return QRectF(0, 0, 10, 20)

    def paint(self, painter, option, widget):
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush(self.color))
        painter.drawPolygon(QPolygonF([QPointF(0,0), QPointF(10,5), QPointF(10,15), QPointF(0,20)]))


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    scene = QGraphicsScene(-200, -200, 400, 400)

    mux = Mux()
    mux.setPos(0, 0)
    scene.addItem(mux)

    view = QGraphicsView(scene)
    view.setRenderHint(QPainter.Antialiasing)
    view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
    view.setBackgroundBrush(QColor(230, 200, 167))
    view.setWindowTitle("Pipelined Microarchitecture")
    view.show()

    
    sys.exit(app.exec_())
