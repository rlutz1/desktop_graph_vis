import sys

from UI.navigation_pane import NavigationPane
from UI.graph_pane import GraphPane
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QPushButton,
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QWidget,
    QTabBar,
    QTabWidget,
    QMainWindow,
    QHBoxLayout,
    QSlider,
    QSpinBox,
)

class MainWindow(QMainWindow): # inherits from QMainWIndow
  
  def setup_window(self):
    self.setWindowTitle("Graph Algorithm Visualizer") # basic title
    self.setMinimumSize(QSize(1000, 500))
    
    central_space = QWidget()
    # central_space.setStyleSheet("")
    layout = QHBoxLayout()
   
    layout.addWidget(NavigationPane(self))
    layout.addWidget(GraphPane(self)) # placeholder
    central_space.setLayout(layout)

    self.setCentralWidget(central_space)


  # def setup_nav_pane(self):
  #   self.setCentralWidget(NavigationPane())


  def __init__(self):
    super().__init__() # call to Qmain window super

    self.setup_window() # setup the window meta info
    # self.setup_nav_pane() # setup the nav pane within the window
    

    # button = QPushButton("Gimme a sexy push")
    # button.setFixedSize(QSize(200, 50))
    # self.setCentralWidget(button) # set the central widget in vanilla layout of main window