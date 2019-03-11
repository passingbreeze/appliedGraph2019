

# https://networkx.github.io/documentation/networkx-1.9.1/reference/algorithms.operators.html

import networkx as nx
import matplotlib.pyplot as plt
import numpy

numpy.random.seed(121)

G = nx.cycle_graph(5)
E = nx.path_graph(5)
W = nx.cartesian_product(G,E)
Q = nx.complement(E)

plt.subplot(221)
nx.draw(G, node_color="y")

plt.subplot(222)
nx.draw(E, node_color="green")

plt.subplot(223)
nx.draw(W,node_color="blue")

plt.subplot(224)
nx.draw(Q, node_color="purple")
plt.show()