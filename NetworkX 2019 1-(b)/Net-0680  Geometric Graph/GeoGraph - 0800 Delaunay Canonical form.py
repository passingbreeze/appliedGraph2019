

# import point data as xy coordinates
points = [(1,2), (10,0),(7,13),(22,5),(1,17),(13,14), \
          (9,23), (10,4), (25,24)]

# make a Delaunay triangulation of the point data
import scipy.spatial
delTri = scipy.spatial.Delaunay(points)

# create a set for edges that are indexes of the points
edges = set()
# for each Delaunay triangle
for n in range(delTri.nsimplex):
    # for each edge of the triangle
    # sort the vertices
    # (sorting avoids duplicated edges being added to the set)
    # and add to the edges set
    edge = sorted([delTri.vertices[n,0], delTri.vertices[n,1]])
    edges.add((edge[0], edge[1]))
    edge = sorted([delTri.vertices[n,0], delTri.vertices[n,2]])
    edges.add((edge[0], edge[1]))
    edge = sorted([delTri.vertices[n,1], delTri.vertices[n,2]])
    edges.add((edge[0], edge[1]))

# --------------------------------------

# make a graph based on the Delaunay triangulation edges
import networkx as nx
graph = nx.Graph(list(edges))
print((graph.edges()))

for node in range( 8 ):
    print("N(",node,")=", graph.neighbors(node))



# plot graph
import matplotlib.pyplot as plt
pointIDXY = dict(list(zip(list(range(len(points))), points)))
nx.draw(graph, pointIDXY)
plt.show()
