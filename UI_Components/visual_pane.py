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


# the entire visualization pane. this contains the 
# visual pane and the interaction area.
class VisualPane(QWidget): # generally a QWidget

  _visual_area = None
  _interaction_area = None

  # sloppy, for testing only:
  _visual_edges = []

  def __init__(self, parent):
    super().__init__(parent) # super initialization
    self._init_visual_area()
    self._init_interaction_area()
    self._init_visual_pane()

    # playground:
    v1 = VertexWidget(self._visual_area, "Iowa")
    v2 = VertexWidget(self._visual_area, "Texas")

    self._visual_area.add_vertex(v1)    
    self._visual_area.add_vertex(v2)  

    self._visual_area.add_edge(v1, v2, 0)

    v3 = VertexWidget(self._visual_area, "Colorado")
    self._visual_area.add_edge(v3, v2, 0)
   
  # initialize the general visual area
  def _init_visual_area(self):
    self._visual_area = VisualArea(self)

  # initialize the button/interaction with visual and sim area
  def _init_interaction_area(self):
    self._interaction_area = InteractionArea(self)

  # initialize the final pane
  def _init_visual_pane(self):
    self.setMinimumSize(self.parent().size())
    layout = QHBoxLayout()
    self.setLayout(layout)
    layout.addWidget(self._visual_area)
    layout.addWidget(self._interaction_area)

  # set the edit button action
  def set_edit_action(self, action):
    return self._interaction_area.set_edit(action)
  
  # set the reset button action
  def set_reset_action(self, action):
    return self._interaction_area.set_reset(action)

 
# encapsulation of the visualization area. 
# TODO this is specific to graph for now.
class VisualArea(QWidget):

  _canvas_container = None
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
  
  def dragEnterEvent(self, e):
    e.accept()

  def dropEvent(self, e):
     e.source().move(e.pos())
     self._update_canvas()
     

  def add_vertex(self, v):
    self.layout().addWidget(v)
    self.layout().setCurrentWidget(v)

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

    print(self._visual_edges)

# encapsulating the simple interaction area
# for the algorithm. 
class InteractionArea(QWidget):
   
  EDIT_ID = "Edit"
  PLAY_ID = "Play"
  STEP_ID = "Step"
  RESET_ID = "Reset"

  _interactions = {
    EDIT_ID: None, 
    PLAY_ID: None, 
    STEP_ID: None,
    RESET_ID: None
    }
                   
  def __init__(self, parent):
    super().__init__(parent) # super initialization
    layout = QVBoxLayout()
    self.setLayout(layout)
    self._init_interactions(layout)
    layout.addStretch() # top heavy layout
    self.setStyleSheet(self._get_interaction_area_style())
  
  # initialize the buttons that will populate the interaction zone
  def _init_interactions(self, layout):
    for i in self._interactions:
      button = InteractionButton(text = i, parent = self)
      self._interactions[i] = button
      layout.addWidget(button)

  # change the stylesheet for the interaction area as a whole
  def _get_interaction_area_style(self):
    return """
      background-color: #a2c8fa; 
      max-width: 150px;
      """
  
  # testing idea
  def set_edit(self, action):
    self._interactions[self.EDIT_ID].add_push_action(action)

  # testing idea
  def set_reset(self, action):
    self._interactions[self.RESET_ID].add_push_action(action)

class InteractionButton(QPushButton):

  _action = None

  def __init__(self, parent, text):
    super().__init__(text = text, parent = parent) # super initialization
    self.setStyleSheet(self._get_interaction_button_style())

  def add_push_action(self, action):
    self._action = action
    self.clicked.connect(self._action.action)
  
  # change style of the interaction buttons
  def _get_interaction_button_style(self):
    return """
      background-color: grey; 
      font: italic 1.5rem "Fira Sans", serif;
      min-height: 30px;
      """
