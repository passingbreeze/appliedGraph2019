# Using a stochastic graph generator, e.g.,
import matplotlib.pyplot as plt
import networkx as nx


er = nx.erdos_renyi_graph(30, 0.15)
nx.draw( er )
plt.show()

ws = nx.watts_strogatz_graph(30, 3, 0.1)
nx.draw( ws )
plt.show()

ba = nx.barabasi_albert_graph(10, 5)
nx.draw( ba )
plt.show()

red = nx.random_lobster(20, 0.9, 0.9)
nx.draw( red )
plt.show()
