

# python 3에서 동작하지 않음

import matplotlib.tri.delaunay as triang
import numpy
import pylab
from scipy.spatial import Delaunay


numpy.random.seed(10)
# 10 random points (x,y) in the plane
x,y =  numpy.array(numpy.random.standard_normal((2,30)))
print (x)
print (y)
cens,edg,tri,neig = triang.tri(x,y)

for t in tri: # t[0], t[1], t[2] are the points indexes of the triangle
    t_i = [t[0], t[1], t[2], t[0]]
    print ( t_i )
    pylab.plot(x[t_i],y[t_i])

pylab.plot(x,y,'o')
pylab.show()

