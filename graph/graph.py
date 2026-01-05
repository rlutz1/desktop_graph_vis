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
    if self.valid_vertex(id, edges):
      self.__vertices.append(Vertex(id, edges))
    # print("todo")

  def add_edge(self, start, end, weight = None): # assuming start and end are id's of vertex
    if self.valid_edge(start, end, weight):
      edge = Edge(start, end, weight)
      self.add_edge_to_vertex(edge)
      self.add_vertex(end)
      self.__edges.append(edge)
    print("todo")

  def add_edge_to_vertex(self, edge):
    id = edge.get_start()
    for v in self.__vertices:
      if v.get_id() == id:
        v.add_edge(edge)
        return

    # vertex was not found in list, make a new one
    self.add_vertex(edge.get_start(), [edge])


  def valid_vertex(self, id, edges):
    # test 1: vertex id is not already in our list
    for v in self.__vertices:
      if v.get_id() == id: return False
    # test 2: edges given all start from this vertex
    for e in edges:
      if e.get_start().get_id() != id: return False

    return True

  def valid_edge(self, start, end, weight):
    # test 1: start and end is not none
    if start is None or end is None: return False
    # test 2: weight is a number, neg, 0, pos are fine generally
    if isinstance(weight) != int and isinstance(weight) != float: return False

    return True


# ============================================================

class Vertex:
  __id = None
  __edges = []

  def __init__(self, id, edges = []):
    self.__edges = edges # TODO: allow multiple edges to same thing. TODO: check if start is this vertex
    __id = id

  def get_id(self):
    return self.__id
  
  def add_edge(self, edge):
    if edge.get_start().get_id() == self.__id:
      self._edges.append(edge)

# ============================================================

class Edge:
  __weight = None
  __start = None
  __end = None

  def __init__(self, start, end, weight = None):
    __weight = weight
    __start = start
    __end = end

  def get_weight(self):
    return self.__weight

  def get_start(self):
    return self.__start
  
  def get_end(self):
    return self.__end

# ============================================================