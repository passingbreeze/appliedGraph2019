# Name:        module1
# Author:      Zoh
# Created:     21-01-2018
#-------------------------------------------------------------------------------

import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_node("a")
G.add_nodes_from(["b","c"])

G.add_edge(1,2)
G.add_edge("book","orange")
edge = ("d", "e")
G.add_edge(*edge)
edge = ("a", "b")
G.add_edge(*edge)
G.add_edge( *(1, "book") )

print("Nodes of graph: ")
print((G.nodes()))
print("Edges of graph: ")
print((G.edges()))

nx.draw(G)
#plt.savefig("simple_path.png") # save as png
plt.show() # display
