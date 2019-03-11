

import matplotlib.pyplot as plt
import matplotlib.tri as tri
import pylab
import numpy
import math


# 10 random points (x,y) in the plane
x,y =  numpy.array(numpy.random.standard_normal((2,30)))
print(x)
print(y)
triang = tri.Triangulation(x, y)
plt.triplot(triang, 'bo-', lw=1)

print(triang)
#for t in triang: # t[0], t[1], t[2] are the points indexes of the triangle
#    t_i = [t[0], t[1], t[2], t[0]]
#    print(t_i)
#    pylab.plot(x[t_i],y[t_i])

pylab.plot(x,y,'o')
pylab.show()