from UI_Components.Graph.graph_visual import VertexWidget

from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QSize
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
    QStackedLayout,
    QVBoxLayout,
    QHBoxLayout,
    QLayout,
    QWidget,
    QTabWidget
)

class VisualPane(QWidget): # generally a QWidget

  _visual_area = None
  _interaction_area = None
  _canvas_container = None
  _interactions = ["Edit", "Play", "Step", "Reset"]

  # sloppy, for testing only:
  _visual_edges = []

  def __init__(self, parent):
    super().__init__(parent) # super initialization
    self._init_visual_area()
    self._init_interaction_area()
    self._init_visual_pane()
    print(self.size())
    
    print(self._visual_area.size())
    print(self._interaction_area.size())
  
  # initialize the general visual area
  def _init_visual_area(self):
    # layout = QStackedLayout()
    # layout = QVBoxLayout()
    # self._visual_area = QWidget(self)
    # self._visual_area.setStyleSheet("min-width: 1000px;")
    # self._visual_area.setAcceptDrops(True)
    # self._visual_area.dragEnterEvent = lambda e: e.accept()
    # self._visual_area.dropEvent = lambda e: e.source().move(e.pos())

    # self._visual_area.setLayout(layout)
    # layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
    self._visual_area = VisualArea(self)

    v1 = VertexWidget(self._visual_area, "Iowa")
    v2 = VertexWidget(self._visual_area, "Texas")

     
    

    # self._visual_area.setMinimumSize(QSize(750, 500)) # TODO: fix this hardcoded sizing sloppiness
   
    # canvas = self._canvas_container.pixmap()

    # layout.addWidget(v1)
    # layout.addWidget(v2)
    self._visual_area.addVertex(v1)    
    self._visual_area.addVertex(v2)  
    # layout.addWidget(self._canvas_container)


    

    # self._visual_area = QLabel()
    # canvas = QPixmap(600, 700)
    # canvas.fill(Qt.GlobalColor.white)
    # self._visual_area.setPixmap(canvas)

    # canvas = self._visual_area.pixmap()
    # painter = QPainter(canvas)
    # painter.drawLine(10, 10, 300, 200)
    # painter.end()
    # self._visual_area.setPixmap(canvas)

  # initialize the button/interaction with visual and sim area
  def _init_interaction_area(self):
    layout = QVBoxLayout()
    self._interaction_area = QWidget(self)
    self._interaction_area.setLayout(layout)
    self._init_interactions(layout)
    layout.addStretch() # top heavy layout
    self._interaction_area.setStyleSheet(self._get_interaction_area_style())
  
  # initialize the buttons that will populate the interaction zone
  def _init_interactions(self, layout):
    for i in self._interactions:
      button = QPushButton(i)
      button.setStyleSheet(self._get_interaction_button_style())
      layout.addWidget(button)

  # initialize the final pane
  def _init_visual_pane(self):
    layout = QHBoxLayout()
    self.setLayout(layout)
    layout.addWidget(self._visual_area)
    layout.addWidget(self._interaction_area)

  # change the stylesheet for the interaction area as a whole
  def _get_interaction_area_style(self):
    return """
      background-color: #a2c8fa; 
      max-width: 150px;
      """
  
  # change style of the interaction buttons
  def _get_interaction_button_style(self):
    return """
      background-color: grey; 
      font: italic 1.5rem "Fira Sans", serif;
      min-height: 30px;
      """

  # def dragEnterEvent(self, e):
  #   e.accept()
  
class VisualArea(QWidget):

  _canvas_container = None

  def __init__(self, parent):
    super().__init__(parent) # super initialization
    self.setMinimumSize(QSize(750, 500))

    self.setAcceptDrops(True)
    # self.dragEnterEvent = lambda e: e.accept()
    # self._visual_area.dropEvent = lambda e: e.source().move(e.pos())
    layout = QStackedLayout()
    self.setLayout(layout)
    layout.setStackingMode(QStackedLayout.StackingMode.StackAll)

    self._canvas_container = QLabel(parent = self)
    canvas = QPixmap(self.size())
    
    canvas.fill(QColor(255, 255, 255))
    self._canvas_container.setPixmap(canvas)
    layout.addWidget(self._canvas_container)
  
  def dragEnterEvent(self, e):
    e.accept()

  def dropEvent(self, e):
     e.source().move(e.pos())

  def addVertex(self, v):
    self.layout().addWidget(v)
    self.layout().setCurrentWidget(v)

  def addEdge(self, v1, v2):
    # this is going to be written as a long script basically, 
    # but needs to be cleaned into clear functionality.
    # below, let's add an edge between v1 and v2.
    # this will mean drawing a line between the 2 to start.

    canvas = self._canvas_container.pixmap()
    painter = QPainter(canvas)
    pen = QPen()
    pen.setWidth(3)
    pen.setColor(QColor(255, 0, 0)) # red for now. 
    painter.setPen(pen)

    painter.drawLine(v1.pos().x(), v1.pos().y(), v2.pos().x(), v2.pos().y())