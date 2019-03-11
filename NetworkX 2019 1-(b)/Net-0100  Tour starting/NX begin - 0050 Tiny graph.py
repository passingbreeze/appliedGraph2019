
import networkx as nx
import matplotlib.pyplot as plt
import math

g = nx.Graph() #empty graph
g.add_node(1)   # A list of nodes
g.add_nodes_from([2, 3])
# A container of nodes

g.add_node('string')
g.add_node(100) # cosine function
g.add_node(200)
print(g.nodes())

g.add_edge(1, 2, score=999)
e=(2,3)
g.add_edge(*e) # unpack tuple
g.add_edges_from([(1, 2), (0,3),(1, 3), (0,'string'), (1,4), (2,100), (3,100)])
g.remove_edge(1, 2)
print(g.nodes())
print(g.edges())

for x in g.nodes() :
    print("x=", x  , "degree=", g.degree( x ) , "이웃=", g[x])

print("out=", g.neighbors(1))

nx.draw(g)  # network을 그림.
plt.show( ) # 그려진 그림을 화면에 matplotlib으로 뿌림

