# ============================================================
# this is generally how we will set up communication back and 
# forth between the front and back end.
# algorithms and UI will have access to this "singleton"
# and communicate via as needed.
# this could be overkill, but have a feeling separating out this 
# communication could avoid muddying the waters later on.
# ============================================================

class Interpreter():

  _algorithm = None
  _visualizer = None

  def __init__(self, algorithm, visualizer):
    self._algorithm = algorithm
    self._visualizer = visualizer

  # expecting a Visual as sent from the algorithm
  # to give to the visualizer in pieces
  def send_visual(self, visuals):
    for id in visuals.ids():
      # send the visualizer the updater along with unique id
      self._visualizer.update_visual(id, visuals[id]) # TODO
    self._visualizer.update() # unsure if this is needed yet or if appropriate
    # i think i need to only update the widgets with changes, not sure if 
    # the paint event "falls" down through the inheritance tree
  
  # notify the algo we are finished. unclear if needed yet.
  # def notify_complete(self):
  #    self._algorithm.notify()