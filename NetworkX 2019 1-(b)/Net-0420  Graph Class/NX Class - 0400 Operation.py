# https://networkx.github.io/documentation/stable/reference/algorithms/operators.html


import matplotlib.pyplot as plt
import networkx as nx

G1 = nx.path_graph(5)
G2 = nx.path_graph(3)
W = nx.path_graph(8)
nx.draw(G1)
plt.show()

#X = subgraph(G, W)      # induced subgraph view of G on nodes in nbunch
Q = nx.union(G1,G2, rename=('G-','H-'))         # graph union
nx.draw(Q)
plt.show()

disjoint_union(G1,G2)    # graph union assuming all nodes are different
cartesian_product(G1,G2) # return Cartesian product graph
compose(G1,G2)           # combine graphs identifying nodes common to both
complement(G)            # graph complement
create_empty_copy(G)     # return an empty copy of the same graph class
convert_to_undirected(G) # return an undirected representation of G
convert_to_directed(G)   #- return a directed representation of G
