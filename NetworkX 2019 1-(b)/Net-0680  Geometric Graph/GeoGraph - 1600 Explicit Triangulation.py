
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri

xy = [[0.3,0.5],
      [0.6,0.8],
      [0.5,0.1],
      [0.1,0.2]]
xy = np.array(xy)

triangles = [[0,2,1],
             [2,0,3]]

triang = mtri.Triangulation(xy[:,0], xy[:,1], triangles=triangles)
plt.triplot(triang, marker="o")

plt.show()