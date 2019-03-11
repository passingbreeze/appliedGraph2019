#-*- coding: cp949 -*-
# Name:        module1
# Author:      Zoh
# Created:     21-01-2018
#-------------------------------------------------------------------------------

import networkx as nx
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

#plt.rc('font', family='C:\Windows\Fonts\나눔바른고딕OTF')
plt.title( '쪼랩 프렌즈')

DG = nx.DiGraph()

DG.add_node( '김연아')
DG.add_node( '손연재')
DG.add_node( '홍길동')
DG.add_node( '윤종신')

DG.add_edge('김연아', '홍길동')
DG.add_edge('홍길동', '윤종신')
DG.add_edge('윤종신', '홍길동')

pos=nx.spring_layout(DG)

nx.draw(DG)
nx.draw_networkx_labels(DG, pos, font_family=font_name, font_size=13)

plt.show()