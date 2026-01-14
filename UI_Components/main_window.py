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
  
  _navigation_pane = None # pane used specifically for navigating through algorithms
  _visual_pane = None # pane used for editing and animating the data struct
  _width = 1000
  _height = 500

  _curr_algorithm = None
  
  
  def __init__(self):
    super().__init__() # call to Qmain window super
    self._init_window() # 1. setup the window meta info
    self._init_actions()# 2. initialize window actions 


  def _init_window(self):
    self.setWindowTitle("Graph Algorithm Visualizer") # basic title
    self.setMinimumSize(QSize(self._width, self._height))
    
    central_space = QWidget(parent = self)
    layout = QHBoxLayout()

    self._navigation_pane = NavigationPane(self)
    self._visual_pane = VisualPane(self)

    layout.addWidget(self._navigation_pane)
    layout.addWidget(self._visual_pane)
    central_space.setLayout(layout)

    self.setCentralWidget(central_space)

  # main window is our "controller", so to speak.
  # it is allowed to attach actions to front end portions.
  def _init_actions(self):
    self.set_edit_action(GraphEditAction())
    # self.set_reset_action(TestAction(self))
    self.set_reset_action(None) # TODO
    self.set_play_action(None) # TODO
    self.set_step_action(None) # TODO
    
  # general access to set the edit action
  def set_edit_action(self, action):
    self._visual_pane.set_edit_action(action)
    
  # general access to set the reset action
  def set_reset_action(self, action):
    self._visual_pane.set_reset_action(action)

  # general access to set the step action
  def set_play_action(self, action):
    self._visual_pane.set_play_action(action)
    
  # general access to set the step action
  def set_step_action(self, action):
    self._visual_pane.set_step_action(action)

  # getters
  def width(self):
    return self._width
  
  def height(self):
    return self._height

# ====================================================================

class Action():

  def __init__(self): 
    pass

  def action(self):
    print("Empty action, should not use this directly. Override in child class.")

# let's focus in on this.
# we need to be able to:
# 1. add a vertex
# 2. remove a vertex
# 3. add an edge
# 4. remove an edge
# and have this both reflected on necessary backend structures
# and provide the visual feedback necessary to correspond.
class GraphEditAction(Action):

  def __init__(self):
    super().__init__()

  def action(self):
    print("It worked!")

class ChangeAction(Action):

  def __init__(self):
    super().__init__()

  def action(self):
    print("CHANGED")

class TestAction(Action):

  _root = None

  def __init__(self, root):
    super().__init__()
    self._root = root


  def action(self):
    print("Test action, reporting for duty")
    self._root.set_edit_action(ChangeAction())




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