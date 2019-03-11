

# https://networkx.github.io/documentation/networkx-1.9.1/reference/algorithms.operators.html

import networkx as nx
import matplotlib.pyplot as plt
import numpy

numpy.random.seed(121)

G = nx.dodecahedral_graph()
edge_labels = nx.draw_networkx_edge_labels(G ,pos=nx.spring_layout(G))

nx.draw( G )
plt.show()
