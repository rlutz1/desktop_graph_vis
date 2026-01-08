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
    self._visual_area = QWidget()

  # initialize the button/interaction with visual and sim area
  def _init_interaction_area(self):
    layout = QVBoxLayout()
    self._interaction_area = QWidget()
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

  def _get_interaction_area_style(self):
    return """
      background-color: #a2c8fa; 
      max-width: 150px;
      """
  
  def _get_interaction_button_style(self):
    return """
      background-color: grey; 
      font: italic 1.5rem "Fira Sans", serif;
      min-height: 30px;
      """

  


