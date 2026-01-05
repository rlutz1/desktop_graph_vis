# very basic classes to help represent an adjacency list style representation of 
# a graph on the backend.

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
    print("todo")

  def add_edge(self, start, end, weight = None):
    print("todo")



class Vertex:
  __id = None
  __edges = []

  def __init__(self, id, edges = []):
    self.__edges = edges
    __id = id


class Edge:
  __weight = None
  __start = None
  __end = None

  def __init__(self, start, end, weight = None):
    __weight = weight
    __start = start
    __end = end