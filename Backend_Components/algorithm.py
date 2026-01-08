# ============================================================
# the purpose of this is to aid in the abstraction of an algorithm as a state machine.
# we will follow the basic definition of what an algorithm is:
# a procedural, finite sequence that solves a specific problem.
# this is the most general form of what the algorithm is and has.
# ============================================================

class Algorithm:

  __beginning_state = None # the special beginning state required
  __sequence = [] # series of finite steps of the algorithm
  __ending_state = None # the special ending state required

  def __init__(self, begin, end, sequence = []):
    if begin is None or end is None:
      print("Beginning and ending state is REQUIRED. Algorithm init is faulty")
    
    self.__beginning_state = begin
    self.__ending_state = end
    self.__sequence = sequence
    print("Algorithm initialized.")

# ============================================================
# this is to represent a general state of the algorithm running.
# an algorithm will be defined as generally a sequence of finite states.
# each state requires an action and a customized visual to play back.
# ============================================================

class State:

  __action = None # the action this state will carry out tangibly on backend structures
  __visual = None # the visual this state will carry out on the front end as a visualization

  def __init__(self, action, visual):
    if action is None:
      print("No action assigned to state, not recommended.")
    
    if visual is None:
      print("No visual assigned to this state--are you sure you want that?")
    
    self.__action = action
    self.__visual = visual
    print("State initialized.")

