
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

points = np.array([[0.2, 0.6], [0, 1.1], [2, 1.7], [2.6, 0.2], \
                   [1.5, 0.73], [1, 1], [3,1.5]])
tri = Delaunay(points)

print("1) ", tri.neighbors[1])
print("2) ", tri.neighbors[1])
print(tri.simplices)
print(points[tri.simplices])

# Triangle 0 is the only neighbor of triangle 1, and it’s opposite to vertex 1 of triangle 1:
print("3) ", tri.neighbors[1])

print("4) ", tri.neighbors[1])
print("5) ", tri.neighbors[1])
print("6) ", points[tri.simplices[1,1]])

p = np.array([(0.1, 0.2), (1.5, 0.5)])
print("7) ", tri.find_simplex(p))




plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'ro')
plt.show()
