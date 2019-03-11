

import sys

import matplotlib.pyplot as plt
import networkx as nx

G = nx.grid_2d_graph(4, 4)  # 5x5 grid

# write edgelist to grid.edgelist
nx.write_edgelist(G, path="grid.edgelist", delimiter=":")
# read edgelist from grid.edgelist
H = nx.read_edgelist(path="grid.edgelist", delimiter=":")

nx.draw(H)

plt.show()