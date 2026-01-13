
from UI_Components.Graph.graph_visual import GraphVisualArea

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

  def __init__(self, parent):
    super().__init__(parent) # super initialization
    self._init_visual_area()
    self._init_interaction_area()
    self._init_visual_pane()
   
  # initialize the general visual area
  def _init_visual_area(self):
    self._visual_area = GraphVisualArea(self)

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
      background-color: red;
      max-width: 150px;
      """
  
  # testing idea
  def set_edit(self, action):
    self._interactions[self.EDIT_ID].add_push_action(action)
    print("???")

  # testing idea
  def set_reset(self, action):
    self._interactions[self.RESET_ID].add_push_action(action)

class InteractionButton(QPushButton):

  _action = None

  def __init__(self, text, parent):
    super().__init__(text = text, parent = parent) # super initialization
    self.setStyleSheet(self._get_interaction_button_style())

  def add_push_action(self, action):
    self._action = action # likely unnecessary.
    self.clicked.connect(self._action.action)
    # self.clicked.connect(action.action)
    # action.action()

  
  # change style of the interaction buttons
  def _get_interaction_button_style(self):
    return """
      background-color: grey; 
      font: italic 1.5rem "Fira Sans", serif;
      min-height: 30px;
      """
