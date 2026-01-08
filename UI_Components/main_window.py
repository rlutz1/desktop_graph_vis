import sys

from UI_Components.navigation_pane import NavigationPane
from UI_Components.visual_pane import VisualPane
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
  

  def __init__(self):
    super().__init__() # call to Qmain window super
    self.setup_window() # setup the window meta info

  def setup_window(self):
    self.setWindowTitle("Graph Algorithm Visualizer") # basic title
    self.setMinimumSize(QSize(1000, 500))
    
    central_space = QWidget()
    # central_space.setStyleSheet("")
    layout = QHBoxLayout()
   
    layout.addWidget(NavigationPane(self))
    layout.addWidget(VisualPane(self)) # placeholder
    central_space.setLayout(layout)

    self.setCentralWidget(central_space)


    # ANIMATION EXAMPLE FOR NOTES

    # class Window(QWidget):
    # def __init__(self):
    #     super().__init__()
    #     self.resize(600, 600)
    #     self.child = QWidget(self)
    #     self.child.setStyleSheet("background-color:red;border-radius:15px;")
    #     self.child.resize(100, 100)
    #     self.anim = QPropertyAnimation(self.child, b"pos")
    #     self.anim.setEndValue(QPoint(200, 200))
    #     self.anim.setDuration(1500)
    #     self.anim_2 = QPropertyAnimation(self.child, b"size")
    #     self.anim_2.setEndValue(QSize(250, 150))
    #     self.anim_2.setDuration(2000)
    #     self.anim_group = QSequentialAnimationGroup() # or for concurrency: self.anim_group = QParallelAnimationGroup()
    #     self.anim_group.addAnimation(self.anim)
    #     self.anim_group.addAnimation(self.anim_2)
    #     self.anim_group.start()