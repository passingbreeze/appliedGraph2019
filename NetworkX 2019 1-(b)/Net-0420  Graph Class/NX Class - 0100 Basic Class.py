
import networkx as nx
import matplotlib.pyplot as plt
import numpy


petersen= nx.petersen_graph()
tutte   = nx.tutte_graph()
maze    = nx.sedgewick_maze_graph()
tet     = nx.tetrahedral_graph()
nx.draw(tutte, node_color="gray")
plt.show()


# classic graphs
K_5=nx.complete_graph(5)
K_3_5=nx.complete_bipartite_graph(3,5)
barbell=nx.barbell_graph(10,10)
lollipop=nx.lollipop_graph(10,20)
nx.draw(K_5, node_color="green")
plt.show()

# random graphs
er=nx.erdos_renyi_graph(40,0.15)
ws=nx.watts_strogatz_graph(40,3,0.1)
ba=nx.barabasi_albert_graph(40,5)
red=nx.random_lobster(40,0.9,0.9)
nx.draw(ba, node_color="blue")
plt.show()
