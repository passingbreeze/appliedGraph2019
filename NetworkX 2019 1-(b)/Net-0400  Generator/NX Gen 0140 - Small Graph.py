
# https://networkx.github.io/documentation/networkx-1.9.1/reference/algorithms.operators.html

import networkx as nx
import matplotlib.pyplot as plt
import numpy

numpy.random.seed(121)

petersen= nx.petersen_graph()
tutte= nx.tutte_graph()
maze = nx.sedgewick_maze_graph()
tet= nx.tetrahedral_graph()


nx.draw( petersen )
plt.show( )
nx.draw( tutte )
plt.show( )
nx.draw( maze )
plt.show( )
nx.draw( tet )
plt.show( )