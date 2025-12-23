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
    QScrollArea,
    QLayout,
    QWidget,
    QTabWidget
)

class NavigationPane(QTabWidget): # generally a QWidget

  __shortest_path_algos = [
    "Bellman-Ford", 
    "Dijkstra", 
    "Floyd-Warshall",
    "Breadth-First Search",
    "testing",
    "yet another",
    "testing",
    "testing",
    "testing",
    "testing",
    "testing",
    "testing",
    "testing",
    "testing",
    "testing"
    ]
  
  __path_finding_algos = [
    "Breadth-First Search",
    "Depth-First Search",
    "A*"
    ]

  def test(self):
    print("test")

  def init_nav(self, algorithms):
    parent = QScrollArea()
    parent.setWidgetResizable(True)
    widget = QWidget()
    # widget = QScrollArea()
    layout = QVBoxLayout()
    layout.addStretch()
    # layout.setSpacing(100)
    # layout.setContentsMargins(0,0,0,0)
    
    
    for a in algorithms:
      button = QPushButton(a)
      button.setFlat(True)
      button.setStyleSheet("border: 5px solid black; background-color: white; min-height: 30px") # width | style | color
      button.clicked.connect(self.test)
      layout.insertWidget(layout.count() - 1, button)

    # layout.addWidget(widget)
    widget.setLayout(layout)
    parent.setWidget(widget)
    return parent


  def init_navs(self):
    # navs = QTabWidget()
    self.setTabPosition(QTabWidget.West)
    # tab_bar.ButtonPosition = LeftSide
    self.addTab(self.init_nav(self.__shortest_path_algos), "Shortest Path")
    self.addTab(self.init_nav(self.__path_finding_algos), "Path Finding") 

  def init_pane(self):
    self.init_navs()
    
    # self.setMinimumSize(250, 500)
    # self.setMaximumSize(250, 500)
    self.setStyleSheet("background-color: #a2c8fa; max-width: 250px;")


  def __init__(self, parent):
    super().__init__(parent) # super initialization

    # idea is to have a layout, list of widgets, add widgets
    # to the layout, set this widget layout to the layout wanted,
    # then add this widget to the window as desired.
    self.init_pane()


