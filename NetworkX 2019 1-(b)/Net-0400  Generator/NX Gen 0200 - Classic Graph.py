

# https://networkx.github.io/documentation/networkx-1.9.1/reference/algorithms.operators.html

import networkx as nx
import matplotlib.pyplot as plt
import numpy

numpy.random.seed(121)

# classic graphs
K_5 = nx.complete_graph(5)
K_3_5 = nx.complete_bipartite_graph(3, 5)
barbell = nx.barbell_graph(10, 10)
lollipop = nx.lollipop_graph(10, 20)


nx.draw( K_5 )
plt.show( )

nx.draw( K_3_5 )
plt.show( )

nx.draw( barbell )
plt.show( )

nx.draw( lollipop )
plt.show( )