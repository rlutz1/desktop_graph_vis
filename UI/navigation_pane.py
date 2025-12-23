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
    QWidget,
)

class NavigationPane(QWidget): # generally a QWidget

  def init_navs(self):
    shortest_path = QComboBox()
    shortest_path.move(0, 0)
    shortest_path.addItems([
      "Bellman-Ford", 
      "Dijkstra", 
      "Floyd-Warshall",
      "Breadth-First Search"
      ])

    path_finding = QComboBox()
    path_finding.addItems([
      "Breadth-First Search",
      "Depth-First Search",
      "A*"
      ])

    navs  = [
      shortest_path,
      path_finding
    ]

    return navs

  def init_pane(self):
    layout = QVBoxLayout() # for now, a vbox is easiest
    navs = self.init_navs()

    for nav in navs:
      layout.addWidget(nav)

    self.setLayout(layout)
    # self.setMinimumSize(250, 500)
    # self.setMaximumSize(250, 500)
    self.setStyleSheet("background-color: #a2c8fa; width: 100%;")


  def __init__(self):
    super().__init__() # super initialization

    # idea is to have a layout, list of widgets, add widgets
    # to the layout, set this widget layout to the layout wanted,
    # then add this widget to the window as desired.
    self.init_pane()


