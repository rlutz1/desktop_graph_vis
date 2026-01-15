from algorithm import Algorithm, State

class IteratorAlgorithm(Algorithm):

  def __init__():
    super().__init__(begin = IteratorBeginState("Placeholder", IteratorBeginVisual()))


class IteratorBeginState(State):

  def __init__(self, action, visual):
    super().__init__(action, visual)

class IteratorBeginVisual():

  def update():
    print("Iterator algorithm is beginning.")

class IteratorEndVisual():

  def update():
    print("Iterator algorithm is ending.")