# 알고리즘 공학론 조환규
# 2차원 점으로부터 들로니 삼각분할을 구성함.
# 2018년 4월에 동작 확인 함.
# 반드시 numpy, scipy, matplotlib을 설치해야 함.
# > pip install PACKAGE
# pip는 %PYTHON%\script\ 에 있으므로 이 위치를 PATH에 포함시키면 편함.
# 최근에 pip가 update되었습니다.


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