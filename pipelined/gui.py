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

def right_top(item):
  return item.pos() + QPointF(item._width, 0)

def right(item):
  return right_top(item).x()

class Port():
  def __init__(self, port):
    super().__init__()
    self.model = port
    self.p = None
    self._width = 0

  def x(self):
    return self.p.x()
  def y(self):
    return self.p.y()
  def pos(self):
    return self.p

  def setPos(self, p):
    self.p = p

  def tryToPosition(self, models_views, views_positioned):
    input = self.model.input
    input_view = models_views[input]
    if input_view not in views_positioned:
      return False

    percent = self.model.port / self.model.input.nr_ports()
    self.setPos( right_top(input_view) + QPointF( 0, (input_view._height - 20) * percent ) ) # TODO y?

    return True

class Line(QGraphicsItem):
  def __init__(self, line):
    super().__init__()
    self.model = line
    self._width = 0 # TODO??

  def tryToPosition(self, models_views, views_positioned):
    print ("FAILED TO POSITION LINE")
    return True # This is a lie! TODO

  def paint(self, painter, option, widget):
    pass

class Mux(QGraphicsItem):
    def __init__(self, mux):
        super().__init__()

        self.model = mux

        self.color = QColor(0, 0, 255)
        self._width = 10

        self.setIncoming(len(mux.inputs))

    def setIncoming(self, incoming):
        self.incoming = incoming
        self._height = 20 + self.incoming * 10

    def boundingRect(self):
        return QRectF(0, 0, self._width, self._height)

    def tryToPosition(self, models_views, views_positioned):
        x_positions = []
        y_positions = []

        for input in self.model.inputs:
          input_view = models_views[input]
          if input_view not in views_positioned:
            return False

          x_positions.append(right(input_view))
          y_positions.append(input_view.y())

        self.setPos( max(x_positions) + 10, y_positions[0] ) # TODO y!
        return True

    def paint(self, painter, option, widget):
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush(self.color))
        painter.drawPolygon(QPolygonF([QPointF(0,0), QPointF(self._width,10), QPointF(self._width, self._height - 10), QPointF(0,self._height)]))

class RegisterFile(QGraphicsItem):
    def __init__(self, regfile):
      super().__init__()

      self.model = regfile

      self._width = 40
      self._height = 150
      self.color = QColor(255, 0, 0)

    def boundingRect(self):
      return QRectF(0, 0, self._width, self._height)

    def tryToPosition(self, models_views, views_positioned):
      assert False # TODO

    def paint(self, painter, option, widget):
      painter.setPen(QPen(Qt.black, 1))
      painter.setBrush(QBrush(self.color))
      painter.drawPolygon(QPolygonF([QPointF(0,0), QPointF(self._width,0), QPointF(self._width, self._height), QPointF(0,self._height)]))

class ALU(QGraphicsItem):
    def __init__(self, alu):
        super().__init__()

        self.model = alu

        self.color = QColor(150, 150, 150)
        self.setScale(4) # TODO: should this be here?

    def boundingRect(self):
        return QRectF(0, 0, 10, 30)

    def tryToPosition(self, models_views, views_positioned):
      s1_view = models_views[self.model.S1]
      s2_view = models_views[self.model.S2]

      if s1_view not in views_positioned or s2_view not in views_positioned:
        return False

      self.setPos( max (right(s1_view), right(s2_view)) + 10, s1_view.y() ) # TODO y

      return True


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
  generic.abstractcomponents.Port: Port,
  generic.abstractcomponents.HardcodedValueLine: Line,
  generic.abstractcomponents.RegisterFile: RegisterFile,
  generic.ALU.ALU: ALU
}

def mapModelsToViews(models):
  modelsToViews = {}
  for m in models:
    modelsToViews[m] = viewMap[m.__class__](m)

  return modelsToViews

def GUI(models):
    """ the first model is the one from which we start drawing """
    regfile = models[0]

    views = mapModelsToViews(models)
    print(views)

    app = QApplication(sys.argv)

    scene = QGraphicsScene(-50, -50, 400, 400)

    regfile_v = views[regfile]
    regfile_v.setPos(0, 0)
    scene.addItem(regfile_v)

    # LOL, very bad computational complexity! TODO FIXME
    done = False
    views_positioned = [regfile_v]
    while not done:
      done = True
      for _, view in views.items():
        if view in views_positioned:
          continue
        if view.tryToPosition( views, views_positioned ):
          views_positioned.append(view)

          print ("Positioned %s to %s" % (str(view), str(view.pos())))

          if isinstance(view, QGraphicsItem):
            scene.addItem(view)
          done = False

    # TODO: assert the positioned views are the same list as all views
    print ("")
    print (views)
    print (views_positioned)

    view = QGraphicsView(scene)
    view.setRenderHint(QPainter.Antialiasing)
    view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
    view.scale(2, 2)
    view.setBackgroundBrush(QColor(230, 200, 167))
    view.setWindowTitle("Pipelined Microarchitecture")
    view.show()

    
    sys.exit(app.exec_())
