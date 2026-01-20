from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QDrag, QPaintEvent
from PyQt5.QtCore import Qt, QPoint, QMimeData, QSize, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QStackedLayout,
    QScrollArea,
    QLayout,
    QWidget,
    QTabWidget
)

# ============================================================
# what we have in here is all widgets needed to create a 
# visual of all components of a graph.
# these are VISUALS ALONE, and have no functionality.
# ============================================================


# encapsulation of the visualization area. 
# TODO this is specific to graph for now.
class GraphVisualArea(QWidget):

  _canvas_container = None
  _visual_vertices = {} # id -> vertexwidget
  _visual_edges = {} # map of vertex to edges stemming from source

  def __init__(self, parent):
    super().__init__(parent) # super initialization
    self.setAcceptDrops(True) # for the drag and drop function
    
    self.setMinimumSize(QSize(750, 500)) # for now, hard coded, TODO

    # init the stack pane layout functionality
    layout = QStackedLayout() 
    self.setLayout(layout)
    layout.setStackingMode(QStackedLayout.StackingMode.StackAll)

    # init the canvas used for drawing the edges 
    self._canvas_container = QLabel(parent = self)
    canvas = QPixmap(self.size())
    
    canvas.fill(QColor(255, 255, 255))
    self._canvas_container.setPixmap(canvas)
    layout.addWidget(self._canvas_container)

    # PLAYGROUND+++++++++++++++++++++++++++++++++++++++++

    v1 = VertexWidget(self, "Iowa")
    v2 = VertexWidget(self, "Texas")
    self.add_vertex(v1)    
    self.add_vertex(v2)  
    self.add_edge(v1, v2, 0)
    v3 = VertexWidget(self, "Colorado")
    self.add_vertex(v3)  
    self.add_edge(v3, v2, 0)

     # PLAYGROUND+++++++++++++++++++++++++++++++++++++++++
  
  # add a new updater to a widget within
  def update_visual(self, id, updater):
    self._visual_vertices[id].set_updater(updater)

  def dragEnterEvent(self, e):
    e.accept()

  def dropEvent(self, e):
     e.source().move(e.pos())
     self._update_canvas()
     
  def animate(self):
    for v in self._visual_vertices:
      self._visual_vertices[v]._animate.emit()

  def add_vertex(self, v):
    self.layout().addWidget(v)
    self.layout().setCurrentWidget(v)
    self._visual_vertices[v.id()] = v # add to id -> v mapping
    print(self._visual_vertices.keys())

  # for the moment, accepts VertexWidgets since this is mostly called
  # when an edge is added/changed
  def add_edge(self, src, dest, weight):
    # below, let's add an edge between v1 and v2.
    # this will mean drawing a line between the 2 to start.

    if src in self._visual_edges: # if we already have this edge
      self._visual_edges.append(dest) # append the destination to list of ongoing
    else: # if we are adding this new edge
      # we don't have src in dictionary, add with dest edge
      self._visual_edges[src] = [dest] 
      
    # now, we need to update the canvas
    self._update_canvas()

  def _update_canvas(self):

    canvas = QPixmap(self.size())
    canvas.fill(QColor(255, 255, 255))
    
    painter = QPainter(canvas)
    pen = QPen()
    pen.setWidth(3)
    pen.setColor(QColor(255, 0, 0)) # red for now. 
    painter.setPen(pen)

    for src in self._visual_edges:
      for dest in self._visual_edges[src]:
        # painter.drawLine(src.pos().x(), src.pos().y(), dest.pos().x(), dest.pos().y())
        painter.drawLine(src.center(), dest.center())

    painter.end()

    self._canvas_container.pixmap().swap(canvas)
    self._canvas_container.update()

    # print(self._visual_edges)


class VertexWidget(QWidget): # Qlabel can hold the canvas

  _animate = pyqtSignal(name = "animate")

  _id = None
  _updater = None # needs to be filled as something to do o a paint event
  _edge_visuals = []
  _canvas_container = None
  _vertex_text = None
  _vertex_size = 100 # px x px
  _half_vertex_size = _vertex_size // 2
  _vertex_width = 3 # px width of the drawn circle
  _background_color = QColor(255, 255, 255) # white by default
  _vertex_color = QColor(0, 0, 0) # black by default

  def __init__(self, parent, text = None): 
    super().__init__(parent) # call to QWidget window super with parent widget
    # self.setStyleSheet("max-width: 100px; max-height: 100px;")
    self.setMaximumSize(QSize(100, 100))
    self.setMinimumSize(QSize(100, 100))
    self._draw_default_vertex(text)
    self._id = text # TODO: naughty!!!

    self._animate.connect(self.animate) # animation signal slotting

  # draw the vertex within this widget. we will use a canvas for more flexibility.
  # very basic for now though.
  def _draw_default_vertex(self, text):
    self._canvas_container = QLabel(parent = self)
    canvas = QPixmap(self._vertex_size, self._vertex_size)
    canvas.fill(self._background_color)
    self._canvas_container.setPixmap(canvas)
    canvas = self._canvas_container.pixmap()

    painter = QPainter(canvas)
    pen = QPen()
    pen.setWidth(self._vertex_width)
    pen.setColor(self._vertex_color) 
    painter.setPen(pen)

    # half_vertex_size = self._vertex_size // 2 # for center of canvas positioning
    circle_radius = self._half_vertex_size - self._vertex_width # for fitting within the canvas including pen size

    painter.drawEllipse(self.center(), circle_radius, circle_radius)
    
    painter.end()
    self._canvas_container.setPixmap(canvas)

    if text is not None:
      layout = QStackedLayout()
      self.setLayout(layout)
      self._vertex_text = QLabel(text, parent = self)
      # self._vertex_text.setStyleSheet("background-color: red;") # for seeing where actual label is
      self._vertex_text.setAlignment(Qt.AlignCenter)
      self._vertex_text.setWordWrap(True)
      self._vertex_text.setMargin(5)

      layout.addWidget(self._vertex_text)
      layout.addWidget(self._canvas_container)
      
      layout.setStackingMode(QStackedLayout.StackingMode.StackAll)      

      # pen.setWidth(1)
      # pen.setColor(QColor(105, 105, 105))
      # painter.setPen(pen)
      # painter.drawText(QPoint(self.pos().x() + self._vertex_width + 2, self.pos().y() + half_vertex_size), text)
    
  def mouseMoveEvent(self, e):
    if e.buttons() == Qt.MouseButton.LeftButton:
        # print("alskdnashdkasm") # for testing only.
        drag = QDrag(self)
        mime = QMimeData()
        drag.setMimeData(mime)

        pixmap = QPixmap(self.size())
        self.render(pixmap)
        drag.setPixmap(pixmap)
        drag.exec_(Qt.DropAction.MoveAction)
        # self.move(e.pos()) # messes her up, do not use, not proper.

  @pyqtSlot()
  def animate(self):
    if self._updater is not None:
      self._updater.update()

  # def paintEvent(self, e: QPaintEvent):
  #   if self._updater is not None:
  #     self._updater.update()

  def set_updater(self, updater):
    self._updater = updater
    self._updater.assign_widget(self)
    print(self._updater)

  # just give it a tuple for start and end, weight can just be number. 
  # we need to draw the line... anything else?
  def add_edge(self, start, end, weight):
    print()

  def center(self):
    # return self.rect().center()
    # half_vertex_size = self._vertex_size // 2 # for center of canvas positioning
    return QPoint(self.pos().x() + self._half_vertex_size, self.pos().y() + self._half_vertex_size)
  
  def id(self):
    return self._id

  # this may not work, but keeping for notes for edges to always be pointing to the center of a vertex:
  # property posᅟ: QPoint
  # This property holds the position of the widget within its parent widget.
  # If the widget is a window, the position is that of the widget on the desktop, including its frame.
  # When changing the position, the widget, if visible, receives a move event ( moveEvent() ) immediately. If the widget is not currently visible, it is guaranteed to receive an event before it is shown.
  # By default, this property contains a position that refers to the origin 
  def get_position(self):
    return self.pos()
  
  def canvas(self):
    return self._canvas_container.pixmap()
  
# # an EDGE visual representation
# class EdgeWidget(QWidget):

#   _canvas_container = None
#   _edge_text = None
#   # __size = 100 # px x px
#   _edge_width = 3 # px width of the drawn line
#   _background_color = QColor(255, 255, 255) # white by default
#   _edge_color = QColor(0, 0, 0) # black by default

#   def __init__(self, parent, weight = None): 
#     super().__init__(parent) # call to QWidget window super with parent widget
#     self.setStyleSheet("")
#     self._draw_edge(weight) 

#   def _draw_edge(self, text):
#     self._canvas_container = QLabel(parent = self)
#     canvas = QPixmap(self._vertex_size, self._vertex_size)
#     canvas.fill(self._background_color)
#     self._canvas_container.setPixmap(canvas)
#     canvas = self._canvas_container.pixmap()

#     painter = QPainter(canvas)
#     pen = QPen()
#     pen.setWidth(self._edge_width)
#     pen.setColor(self._edge_color) 
#     painter.setPen(pen)

#     half_vertex_size = self._vertex_size // 2 # for center of canvas positioning
#     circle_radius = half_vertex_size - self._vertex_width # for fitting within the canvas including pen size
#     center = QPoint(self.pos().x() + half_vertex_size, self.pos().y() + half_vertex_size)
#     painter.drawEllipse(center, circle_radius, circle_radius)
    
#     painter.end()
#     self._canvas_container.setPixmap(canvas)

#     if text is not None:
#       layout = QStackedLayout()
#       self.setLayout(layout)
#       self._vertex_text = QLabel(text, parent = self)
#       # self._vertex_text.setStyleSheet("background-color: red;") # for seeing where actual label is
#       self._vertex_text.setAlignment(Qt.AlignCenter)
#       self._vertex_text.setWordWrap(True)
#       self._vertex_text.setMargin(5)

#       layout.addWidget(self._vertex_text)
#       layout.addWidget(self._canvas_container)
      
#       layout.setStackingMode(QStackedLayout.StackingMode.StackAll)

