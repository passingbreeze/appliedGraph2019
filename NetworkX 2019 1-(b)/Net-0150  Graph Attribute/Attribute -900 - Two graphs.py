
import networkx as nx
import matplotlib.pyplot as plt
import numpy

numpy.random.seed(11)

G = nx.cycle_graph(8)
E = nx.complete_bipartite_graph(4,3)

fig, myax = plt.subplots()
nx.draw(G, ax = myax )
nx.draw(E, ax = myax, node_color='k' )
plt.show()