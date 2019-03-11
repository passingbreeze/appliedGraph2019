

import matplotlib.pyplot as plt
import networkx as nx

G=nx.DiGraph()
# Add nodes by specifying their positions
G.add_node('10', pos=(2, 10))
G.add_node('9',  pos=(4, 9))
G.add_node('8',  pos=(0, 13))
G.add_node('7',  pos=(1.5, 4))
G.add_node('6',  pos=(4, 4))
G.add_node('5',  pos=(6, 11))
G.add_node('3',  pos=(6, 6))
G.add_node('0',  pos=(0, 0))
# Add edges by defining weight and label
G.add_edge('10','9',weight=  1, label='i')
G.add_edge('10','8',weight= 21, label='ii')
G.add_edge('10','7',weight=  3, label='x')
G.add_edge('9','3' ,weight=  7, label='o')
G.add_edge('9','6' ,weight=-11, label='w')
G.add_edge('9','5' ,weight= 34, label='%')
G.add_edge('7','0' ,weight=  9, label='good')
G.add_edge('7','6' ,weight=23.08, label='gogo')
G.add_edge('6','3' ,weight= 10, label='pop')
G.add_edge('5','3' ,weight= 8,  label='(())')

elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5] # solid edge
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5] # dashed edge

# Retrieve the positions from graph nodes and save to a dictionary
pos=nx.get_node_attributes(G,'pos')
# Draw nodes
nx.draw_networkx_nodes(G,pos,node_size=700, node_color='orange')

# Draw edges
nx.draw_networkx_edges(G,pos,edgelist=elarge, width=2, edge_color='g')
nx.draw_networkx_edges(G,pos,edgelist=esmall, arrows=False, width=5,
                       alpha=0.5,edge_color='b',style='dashed')

# Draw node labels
nx.draw_networkx_labels(G,pos,font_size=18,font_family='sans-serif')

# Draw edge labels
edge_labels =dict([((u, v), d['label'])
                   for u, v, d in G.edges(data=True)])

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.axis('off')
plt.show() # display
