# ============================================================
# the purpose of this is to aid in the abstraction of an algorithm as a state machine.
# we will follow the basic definition of what an algorithm is:
# a procedural, finite sequence that solves a specific problem.
# this is the most general form of what the algorithm is and has.
# ============================================================

class Algorithm:

  _beginning_state = None # the special beginning state required
  _sequence = [] # series of finite steps of the algorithm
  _ending_state = None # the special ending state required

  def __init__(self, begin, end, sequence = []):
    if begin is None or end is None:
      print("Beginning and ending state is REQUIRED. Algorithm init is faulty")
    
    self._beginning_state = begin
    self._ending_state = end
    self._sequence = sequence
    print("Algorithm initialized.")

  # the main method to override and specify the run. 
  # this could be general enough to implement here
  # since it will mainly be the running through of 
  # sequences, communicating with interpreter
  # and awaiting the end of the animation call from interp.
  def run(self):
    pass

# ============================================================
# this is to represent a general state of the algorithm running.
# an algorithm will be defined as generally a sequence of finite states.
# each state requires an action and a customized visual to play back.
# ============================================================

class State:

  _action = None # the action this state will carry out tangibly on backend structures
  _visual = None # the visual this state will carry out on the front end as a visualization

  def __init__(self, action, visual):
    if action is None:
      print("No action assigned to state, not recommended.")
    
    if visual is None:
      print("No visual assigned to this state--are you sure you want that?")
    
    self._action = action
    self._visual = visual
    print("State initialized.")


# ============================================================
# we're gonna focus for a moment on the visualization here.
# a visual is essentially just a mapping of ID's that identify
# uniquely a changeable component on the front end to an 
# Updater. this visual is to be given to the interpretation layer
# between the back and front end so it can hand off appropriately to 
# the visuals.
# ============================================================

class Visual():

  _visuals = {}

  def __init__(self):
    pass

  # add an updater for this widget on the front end.
  # one rule right now: only one updater allowed
  # to keep things simpler.
  def add_visual(self, id, updater):
    self._visuals[id] = updater

  def visuals(self):
    return self._visuals
  
  def ids(self):
    return self._visuals.keys()
  

# ============================================================
# let's talk updater. an updaters job is simply to have an 
# update function that says how to visually change the parent.
# it is up to the developers capability to know what the 
# widget being changed is and specify accordingly.
# this is handed to the front end with the id, which is then taken, 
# the parent is assigned to the front end and then "installed"
# in the front end widget to call .update() on a paint event occurrence.
# ============================================================

class Update():

  _widget = None # the front end widget to change

  def __init__(self):
    pass

  # this the method that should always be overriden 
  # by a child updater.
  def update(self):
    pass

  def assign_widget(self, widget):
    self._widget = widget

# ============================================================
# unclear yet if this will be necessary or anything.
# abstraction of the action a state can have.
# overried the action() function to define any backend upkeep as 
# needed.
# ============================================================

class Action():

  _algorithm = None # the front end widget to change

  def __init__(self):
    pass

  # this the method that should always be overriden 
  # by a child updater.
  def act(self):
    pass

  def assign_algorithm(self, algorithm):
    self._algorithm = algorithm
