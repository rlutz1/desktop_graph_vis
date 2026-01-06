# ============================================================
# very basic classes to help represent an adjacency list style representation of 
# a graph on the backend.
# ============================================================

class Graph:
  __vertices = []
  __edges = []
  __weighted = False
  __directed = False

  # basic construction of the graph
  # NOTE: no error checking currently happening. pinky promise it's okay for now.
  def __init__(self, vertices = [], edges = [], weighted = False, directed = False):
    self.__vertices = vertices # TODO: check for distinct vertex ids here? or ust prcoess to remove duplicates
    self.__edges = edges # TODO: should really also check for any vertices to create based on this
    self.__weighted = weighted
    self.__directed = directed
    print("Graph initialized.")
  
  # main access point to add a vertex with some verification.
  def add_vertex(self, id, edges):
    print(id, " ", edges)
    if self.valid_vertex(id, edges): # problem is here
      self.__vertices.append(Vertex(id, edges))

  # main access point to add an edge to the graph with 
  # verification AND some allowance of vertex on the fly creation
  def add_edge(self, start, end, weight): # assuming start and end are id's of vertex
    if self.valid_edge(start, end, weight):
      edge = Edge(start, end, weight)
      self.add_edge_to_vertex(edge, start) # add this edge to the start vertex's list of edges (or create start as needed)
      self.add_vertex(end, []) # create the end vertex if needed
      self.__edges.append(edge) # append the edge to the graph's ongoing list of edges

  # helper function to attach and edge to a vertex OR create with new edge as needed 
  def add_edge_to_vertex(self, edge, id):
    for v in self.__vertices:
      if v.get_id() == id:
        v.add_edge(edge)
        return

    # vertex was not found in list, make a new one
    self.add_vertex(id, [edge])

  # vertex validation, add tests as needed, to curb dumb developer
  def valid_vertex(self, id, edges):
    # test 1: vertex id is not already in our list
    for v in self.__vertices:
      if v.get_id() == id: return False
    # test 2: edges given all start from this vertex
    for e in edges:
      if e.get_start_id() != id: return False
    
    return True # passed all verification cases

  # edge validation, add tests as needed, to curb dumb developer
  def valid_edge(self, start, end, weight):
    # test 1: start and end is not none
    if start is None or end is None: return False
    # test 2: weight is a number, neg, 0, pos are fine generally (messily done, but)
    if self.__weighted and isinstance(weight) != int and isinstance(weight) != float: return False

    return True # passed all verification cases

  # print func for simple console printing of the graph
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

# ============================================================

class Vertex:
  __id = None
  __edges = []

  def __init__(self, id, edges):
    self.__id = id
    self.__edges = edges
    # for e in edges: # TODO: this is causing problems. adds all edges to all vertices
    #   self.add_edge(e)
    
  def get_id(self):
    return self.__id
  
  def add_edge(self, edge):
    if edge.get_start_id() == self.__id:
      self.__edges.append(edge)

  # TODO: remove edge
  
  def print(self):
    if self.__edges:
      for e in self.__edges:
        print("(", e.get_start_id(), ", ", e.get_end_id(), ")")
    else:
      print("This vertex has no edges.")

# ============================================================

class Edge:
  __weight = None
  __start_id = None
  __end_id = None

  def __init__(self, start, end, weight):
    self.__weight = weight
    self.__start_id = start
    self.__end_id = end

  def get_weight(self):
    return self.__weight

  def get_start_id(self):
    return self.__start_id
  
  def get_end_id(self):
    return self.__end_id
  
  def print(self):
    print("(", self.__start_id, ", ", self.__end_id, ", ", self.__weight, ")")

# ============================================================