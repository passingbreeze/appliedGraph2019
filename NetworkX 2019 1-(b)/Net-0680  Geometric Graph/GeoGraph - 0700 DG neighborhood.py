

import scipy.spatial
import numpy
import pylab

def find_neighbors(pindex, triang):
    return triang.vertex_neighbor_vertices[1] \
    [triang.vertex_neighbor_vertices[0] \
    [pindex]:triang.vertex_neighbor_vertices[0][pindex+1]]


x_list = numpy.random.random(200)
y_list = numpy.random.random(200)

tri = scipy.spatial.Delaunay(numpy.array([[x,y] for x,y in zip(x_list, y_list)]))

pindex = 17

neighbor_indices = find_neighbors(pindex,tri)

pylab.plot(x_list, y_list, 'b.')
pylab.plot(x_list[pindex], y_list[pindex], 'x')
pylab.plot([x_list[i] for i in neighbor_indices],
           [y_list[i] for i in neighbor_indices], 'ro')

pylab.show()