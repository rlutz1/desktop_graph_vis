# ============================================================
# very basic classes to help represent an adjacency list style representation of 
# a graph on the backend.
# ============================================================

class Graph:
  __vertices = []
  __edges = []
  __weighted = False
  __directed = False

  def __init__(self, vertices = [], edges = [], weighted = False, directed = False):
    self.__vertices = vertices # TODO: check for distinct vertex ids here?
    self.__edges = edges
    self.__weighted = weighted
    self.__directed = directed
    print("Graph initialized.")
  
  def add_vertex(self, id, edges = []):
    # print(id)
    if self.valid_vertex(id, edges): # problem is here
      self.__vertices.append(Vertex(id, edges))
    # print("todo")

  def add_edge(self, start, end, weight = None): # assuming start and end are id's of vertex
    if self.valid_edge(start, end, weight):
      edge = Edge(start, end, weight)
      # edge.print()
      self.add_edge_to_vertex(edge)
      self.add_vertex(end, [])
      self.__edges.append(edge)
    # print("todo")

  def add_edge_to_vertex(self, edge):
    id = edge.get_start()
    for v in self.__vertices:
      if v.get_id() == id:
        v.add_edge(edge)
        return

    # vertex was not found in list, make a new one
    self.add_vertex(id, [edge])


  def valid_vertex(self, id, edges):
    # test 1: vertex id is not already in our list
    for v in self.__vertices:
      if v.get_id() == id: return False
    # print(id)
    # test 2: edges given all start from this vertex
    # print(edges)
    for e in edges:
      if e.get_start() != id: return False
    

    return True

  def valid_edge(self, start, end, weight):
    # test 1: start and end is not none
    if start is None or end is None: return False
    # test 2: weight is a number, neg, 0, pos are fine generally
    if self.__weighted and isinstance(weight) != int and isinstance(weight) != float: return False

    return True

  def print(self):
    print("++++++++++++++++++++")
    if not self.__vertices:
      print("This is an empty graph.")
      print("++++++++++++++++++++")
      return

    for v in self.__vertices:
      print("Vertex ", v.get_id(), " has edges:")
      v.print()
      print("++++++++++++++++++++")

    # print(self.__vertices) # TODO: the last one at end is not being added.

# ============================================================

class Vertex:
  __id = None
  __edges = []

  def __init__(self, id, edges = []):
    self.__edges = edges # TODO: allow multiple edges to same thing. TODO: check if start is this vertex
    self.__id = id

  def get_id(self):
    return self.__id
  
  def add_edge(self, edge):
    if edge.get_start() == self.__id:
      self.__edges.append(edge)

  # TODO: remove edge
  
  def print(self):
    if self.__edges:
      for e in self.__edges:
        print("(", e.get_start(), ", ", e.get_end(), ")")
    else:
      print("This vertex has no edges.")

# ============================================================

class Edge:
  __weight = None
  __start = None
  __end = None

  def __init__(self, start, end, weight = None):
    self.__weight = weight
    self.__start = start
    self.__end = end

  def get_weight(self):
    return self.__weight

  def get_start(self):
    return self.__start
  
  def get_end(self):
    return self.__end
  
  def print(self):
    print("(", self.__start, ", ", self.__end, ", ", self.__weight, ")")

# ============================================================