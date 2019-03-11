
import networkx as nx
import matplotlib.pyplot as plt

_,ax = plt.subplots(1,3, figsize=(10,8))
G = nx.Graph()
G.add_nodes_from([0,1,3])
G.add_edge(0,3)
G.add_edge(1,3)
nx.draw_networkx(G, ax=ax[0], title='G')

H = nx.Graph()
H.add_nodes_from([1,2,3,4])
H.add_edges_from([(1,2), (3,4), (1,4)])
nx.draw_networkx(H, ax=ax[1])

U = nx.union(G, H, rename=('G-','H-'))
nx.draw_networkx(U, ax=ax[2])
print(U.nodes())

plt.show()
