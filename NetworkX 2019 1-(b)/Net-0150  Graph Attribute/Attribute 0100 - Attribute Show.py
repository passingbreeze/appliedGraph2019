
import networkx as nx
import matplotlib.pyplot as plt
import math

G = nx.Graph(day="Friday")
print (G.graph)

G.add_node('string')
G.add_node(1, time='5pm')
G.node[1]['room'] = 714
G.add_node(2)
G.add_node(3)
G.add_node(4)
print(G.nodes())

G.add_edge(1, 2, score=999)
G.add_edge(1, 2, weight=4.7 )
G.add_edges_from([(3,4),(4,5)], color='red')
G.add_edges_from([(1,2,{'color':'blue'}), (2,3,{'weight':8})])
G[1][2]['weight'] = 4.7

e=(2,3)
G.add_edge(*e) # unpack tuple
G.add_edges_from([(1, 2), (1, 3), (1,'string'), (1,4), (2,2), (3,4)])

for x in G.nodes() :
    print("x=", x  , "degree=", G.degree( x ) , "이웃=", G[x])

print("out=", G.neighbors(1))

nx.draw(G)  # network을 그림.
plt.show( ) # 그려진 그림을 화면에 matplotlib으로 뿌림

