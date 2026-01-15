from algorithm import Algorithm, State, Visual, Update, Action

class TesterAlgorithm(Algorithm):

  def __init__(self):
    super().__init__(
      begin = TesterBeginState(self),
      end = TesterEndState(self)
      )
    self._init_sequence()
    
  # my guess is that this will need customization depnding on number 
  # of states and the data structures under the hood.
  # for this algorithm, we are just doing some testing to see 
  # how this can work.
  # the only thing we are doing is changing the hardcoded CO
  # vertex to green, then to red, with ending being back to black.
  def _init_sequence(self):
    pass


  # def run(self):
  #   for s in self.

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