from ..algorithm import Algorithm, State, Visual, Update, Action
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QDrag
from PyQt5.QtCore import Qt, QPoint, QMimeData, QSize, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QLabel, QWidget

class TesterAlgorithm(Algorithm):

  def __init__(self, interpreter):
    super().__init__(
      begin = TesterBeginState(self),
      end = TesterEndState(self), 
      interpreter = interpreter
      )
    self._init_sequence()
    
  # my guess is that this will need customization depnding on number 
  # of states and the data structures under the hood.
  # for this algorithm, we are just doing some testing to see 
  # how this can work.
  # the only thing we are doing is changing the hardcoded CO
  # vertex to green, then to red, with ending being back to black.
  def _init_sequence(self):
    self._sequence = [self._beginning_state]
    # somehting something something
    
    # (2) move it
    self._sequence.append(TesterMoveVertexState(self))
    # (1) turn the colorado vertex green
    self._sequence.append(TesterTurnGreenState(self))
    self._sequence.append(self._ending_state)
    
  # main method to "run the algorithm".
  # implementing here for now since i want to isolate in testing
  # field. however, could likely be implemented in Algorithm instead
  def run(self):
    for s in self._sequence:
      self._interpreter.send_visual(s.visuals())
      s.act()


# the state representing the highlighting of the colorado vertex as green
class TesterTurnGreenState(State):
   
  def __init__(self, algorithm):
    super().__init__(self.TesterTurnGreenAction(algorithm), self.TesterTurnGreenVisual())
  
  # VISUAL OF THE STATE
  class TesterTurnGreenVisual(Visual):

    def __init__(self):
      super().__init__()
      self._init_visuals()

    def _init_visuals(self):
      self.add_visual("Colorado", self.TesterTurnGreenUpdate())
      
    class TesterTurnGreenUpdate(Update):
      def __init__(self):
        super().__init__()
      
      # the goal is to redraw the outside of the widget as green.
      # widget here should be a VertexWidget
      def update(self):
        try:
          canvas = self._widget.canvas()
          painter = QPainter(canvas)
          pen = QPen()
          pen.setWidth(3)
          pen.setColor(QColor(0, 255, 0)) # all green 
          painter.setPen(pen)
          painter.drawEllipse(self._widget.center(), 47, 47) # TODO: naughty!
          painter.end()
          self._widget.update()
        except AttributeError:
          print("Widget was not assigned likely!")


  # ACTION OF THE STATE
  class TesterTurnGreenAction(Action):

    def __init__(self, algorithm):
      super().__init__()
      self.assign_algorithm(algorithm)

    def act(self):
      print("I am turning the Colorado vertex green.")

# one other state: move the vertex widget to an arbitrary spot.
# this is really to test if the algorithm needs to run on its
# own thread or if it's enough to just queue events via the
# qt update() call and execution thread.
# also good for testing "different states"
class TesterMoveVertexState(State):
   
  def __init__(self, algorithm):
    super().__init__(self.TesterMoveVertexAction(algorithm), self.TesterMoveVertexVisual())
  
  # VISUAL OF THE STATE
  class TesterMoveVertexVisual(Visual):

    def __init__(self):
      super().__init__()
      self._init_visuals()

    def _init_visuals(self):
      self.add_visual("Colorado", self.TesterMoveVertexUpdate())
      
    class TesterMoveVertexUpdate(Update):
      def __init__(self):
        super().__init__()
      
      # the goal is to redraw the outside of the widget as green.
      # widget here should be a VertexWidget
      def update(self):
        try:
          w = self._widget.parent()
          w.anim = QPropertyAnimation(self._widget, b"pos")
          w.anim.setEasingCurve(QEasingCurve.InOutCubic)
          w.anim.setEndValue(QPoint(100, 100))
          w.anim.setDuration(1500)
          w.anim.start()
        except AttributeError:
          print("Widget was not assigned likely!")


  # ACTION OF THE STATE
  class TesterMoveVertexAction(Action):

    def __init__(self, algorithm):
      super().__init__()
      self.assign_algorithm(algorithm)

    def act(self):
      print("I am MOVING the Colorado vertex.")


# the required beginning state of the algorithm.
class TesterBeginState(State):

  def __init__(self, algorithm):
    super().__init__(self.TesterBeginAction(algorithm), self.TesterBeginVisual())
  
  # VISUAL OF THE STATE
  class TesterBeginVisual(Visual):

    def __init__(self):
      super().__init__()

  # ACTION OF THE STATE
  class TesterBeginAction(Action):

    def __init__(self, algorithm):
      super().__init__()
      self.assign_algorithm(algorithm)

    def act(self):
      print("Beginning action of the tester.")

# the required ending state of the algorithm
class TesterEndState(State):
  
  def __init__(self, algorithm):
    super().__init__(self.TesterEndAction(algorithm), self.TesterEndVisual())

  # VISUAL OF THE STATE
  class TesterEndVisual(Visual):

    def __init__(self):
      super().__init__()

  # ACTION OF THE STATE
  class TesterEndAction(Action):

    def __init__(self, algorithm):
      super().__init__()
      self.assign_algorithm(algorithm)

    def act(self):
      print("End action of the tester.")