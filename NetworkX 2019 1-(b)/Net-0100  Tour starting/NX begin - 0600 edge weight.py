
# Name:        module1
# Author:      Zoh

import networkx as nx
import pylab


G = nx.Graph()
G.add_edge(1, 2, weight=-23)
G.add_edge(2, 3, weight=32)
G.add_edge(1, 3, weight=50)
G.add_edge(1, 4, weight=15)
G.add_edge(2, 5, weight=4)

pos=nx.random_layout(G)
# version 1
pylab.figure(1)
nx.draw(G,pos)
# use default edge labels
nx.draw_networkx_edge_labels(G,pos)

# version 2
pylab.figure(2)
nx.draw(G,pos)
# specifiy edge labels explicitly
edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)

# show graphs
pylab.show()
