from graph import Graph

graph_1 = Graph()
graph_1.print()
# ++++++++++++++++++++
# This is an empty graph.
# ++++++++++++++++++++

graph_1.add_edge("Iowa", "Chicago", 0)
graph_1.print()
# ++++++++++++++++++++
# Vertex  Iowa  has edges:
# ( Iowa ,  Chicago )
# ++++++++++++++++++++
# Vertex  Chicago  has edges:
# This vertex has no edges.
# ++++++++++++++++++++

graph_1.add_edge("Iowa", "Chicago", 0)
graph_1.print()

# ++++++++++++++++++++
# Vertex  Iowa  has edges:
# ( Iowa ,  Chicago )
# ( Iowa ,  Chicago )
# ++++++++++++++++++++
# Vertex  Chicago  has edges:
# This vertex has no edges.
# ++++++++++++++++++++

graph_1.add_edge("Chicago", "1", 0)
graph_1.print()

# ++++++++++++++++++++
# Vertex  Iowa  has edges:
# ( Iowa ,  Chicago )
# ( Iowa ,  Chicago )
# ++++++++++++++++++++
# Vertex  Chicago  has edges:
# ( Chicago ,  1 )
# ++++++++++++++++++++
# Vertex  1  has edges:
# This vertex has no edges.
# ++++++++++++++++++++

graph_1.add_edge("1", "2", 0)
graph_1.print()

# ++++++++++++++++++++
# Vertex  Iowa  has edges:
# ( Iowa ,  Chicago )
# ( Iowa ,  Chicago )
# ++++++++++++++++++++
# Vertex  Chicago  has edges:
# ( Chicago ,  1 )
# ++++++++++++++++++++
# Vertex  1  has edges:
# ( 1 ,  2 )
# ++++++++++++++++++++
# Vertex  2  has edges:
# This vertex has no edges.
# ++++++++++++++++++++

graph_1.add_edge("1", "3", 0)
graph_1.print()

# ++++++++++++++++++++
# Vertex  Iowa  has edges:
# ( Iowa ,  Chicago )
# ( Iowa ,  Chicago )
# ++++++++++++++++++++
# Vertex  Chicago  has edges:
# ( Chicago ,  1 )
# ++++++++++++++++++++
# Vertex  1  has edges:
# ( 1 ,  2 )
# ( 1 ,  3 )
# ++++++++++++++++++++
# Vertex  2  has edges:
# This vertex has no edges.
# ++++++++++++++++++++
# Vertex  3  has edges:
# This vertex has no edges.
# ++++++++++++++++++++

graph_1.add_edge("Chicago", "Iowa", 0)
graph_1.print()

# ++++++++++++++++++++
# Vertex  Iowa  has edges:
# ( Iowa ,  Chicago )
# ( Iowa ,  Chicago )
# ++++++++++++++++++++
# Vertex  Chicago  has edges:
# ( Chicago ,  1 )
# ( Chicago ,  Iowa )
# ++++++++++++++++++++
# Vertex  1  has edges:
# ( 1 ,  2 )
# ( 1 ,  3 )
# ++++++++++++++++++++
# Vertex  2  has edges:
# This vertex has no edges.
# ++++++++++++++++++++
# Vertex  3  has edges:
# This vertex has no edges.
# ++++++++++++++++++++

# graph_1.remove_vertex("Chicago")
# graph_1.print()

# ++++++++++++++++++++
# Vertex  Iowa  has edges:
# This vertex has no edges.
# ++++++++++++++++++++
# Vertex  1  has edges:
# ( 1 ,  2 )
# ( 1 ,  3 )
# ++++++++++++++++++++
# Vertex  2  has edges:
# This vertex has no edges.
# ++++++++++++++++++++
# Vertex  3  has edges:
# This vertex has no edges.
# ++++++++++++++++++++

# graph_1.remove_vertex("1")
# graph_1.print()

# ++++++++++++++++++++
# Vertex  Iowa  has edges:
# This vertex has no edges.
# ++++++++++++++++++++
# Vertex  2  has edges:
# This vertex has no edges.
# ++++++++++++++++++++
# Vertex  3  has edges:
# This vertex has no edges.
# ++++++++++++++++++++

# graph_1.remove_vertex("2")
# graph_1.print()

graph_1.remove_vertex("Iowa")
graph_1.print()

graph_1.add_vertex("Iowa", [])
graph_1.print()

graph_1.add_edge("1", "Iowa", 2)
graph_1.print()