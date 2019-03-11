
from scipy.spatial import Delaunay
import networkx as nx

# nodes and positions
nodes = list('abcdefghi')
points = [(1,2), (10,0),(7,13),(22,5),(1,17),(13,14), \
          (9,23), (10,4), (25,24)]
t = Delaunay(points)
edges = []

m = dict(enumerate(nodes)) # mapping from vertices to nodes
for i in range(t.nsimplex):
    edges.append( (m[t.vertices[i,0]], m[t.vertices[i,1]]) )
    edges.append( (m[t.vertices[i,1]], m[t.vertices[i,2]]) )
    edges.append( (m[t.vertices[i,2]], m[t.vertices[i,0]]) )

print("edge list=\n", edges)

# build graph
G = nx.Graph(edges)
pos = dict(list(zip(nodes,points)))

# draw
import matplotlib.pyplot as plt
nx.draw(G,pos)
plt.show()
