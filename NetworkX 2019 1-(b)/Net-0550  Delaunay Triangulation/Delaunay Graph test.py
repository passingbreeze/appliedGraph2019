import numpy as np

points = np.array([[10, 3], [7, 5], [1, 4], [6, 1], [8,8], [5,5], [11,4], [3,10], [7,2], [4,9],[12,5]])
from scipy.spatial import Delaunay
tri = Delaunay(points)

import matplotlib.pyplot as plt
plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.show()