# 2018년 4월에 동작 확인 함.

import numpy as np
import matplotlib.pyplot as plt
from   scipy.spatial import Delaunay

# 입력 점은 2차원 점입니다. 배열에 넣습니다.
points = np.array([[10, 3], [7, 5], [1, 4], [6, 1], [8,8], \
                   [5,5], [11,4], [3,10], [7,2], [4,9],[12,5]])

tri = Delaunay(points)  # 들로니 삼각분할을 하고 그래프를 생성함.

plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'ro') #ro는 red o 마커

print ("tri.simplices List( 3 points) ")
for i, samgak in enumerate(tri.simplices) :
    print ("Triangle[",i, "]",  samgak)


print ("\n\n P(x,y) = ")
for i, myp in enumerate(points[tri.simplices]) :
    print ("Tr", i, "=",  myp[0],  myp[1],  myp[2])


plt.show()