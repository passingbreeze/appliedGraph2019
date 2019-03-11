# Attributes
#
# points (ndarray of double, shape (npoints, ndim)) Coordinates of input points.
# vertices (ndarray of double, shape (nvertices, ndim)) Coordinates of the Voronoi vertices.
# ridge_points (ndarray of ints, shape (nridges, 2)) Indices of the points between which each Voronoi ridge lies.
# ridge_vertices (list of list of ints, shape (nridges, *)) Indices of the Voronoi vertices forming each Voronoi ridge.
# regions (list of list of ints, shape (nregions, *)) Indices of the Voronoi vertices forming each Voronoi region. -1 indicates vertex outside the Voronoi diagram.
# point_region (list of ints, shape (npoints)) Index of the Voronoi region for each input point. If qhull option “Qc” was not specified, the list will contain -1 for points that are not associated with a Voronoi region.

# Methods

#add_points(points[, restart]) Process a set of additional new points.
#close() Finish incremental processing.


import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np

points = np.array([[17, 2], [7, 3], [11, 3], [6, 7], [1, 2], [4, 12],   \
                  [12, 10], [9, 13], [5, 12]])

vor = Voronoi(points)
print(vor.vertices)
print(vor.regions)

# There is a single finite Voronoi region, and four finite Voronoi ridges:
print(vor.ridge_vertices)
print(vor.ridge_points)
# The ridges are perpendicular between lines drawn between the following input points:


voronoi_plot_2d(vor)
plt.show()


