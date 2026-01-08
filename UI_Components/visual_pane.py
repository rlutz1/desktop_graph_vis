from UI_Components.Graph.graph_visual import VertexWidget

from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt
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
  _interactions = ["Edit", "Play", "Step", "Reset"]

  def __init__(self, parent):
    super().__init__(parent) # super initialization
    self._init_visual_area()
    self._init_interaction_area()
    self._init_visual_pane()
  
  # initialize the general visual area
  def _init_visual_area(self):
    layout = QStackedLayout()
    # layout = QVBoxLayout()
    self._visual_area = QWidget(self)
    self._visual_area.setLayout(layout)
    layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
    layout.addWidget(VertexWidget(self._visual_area, "something a little different as well as pie"))
    layout.addWidget(VertexWidget(self._visual_area, "Texas"))
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

  


