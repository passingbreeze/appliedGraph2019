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

#plt.rc('font', family='C:\Windows\Fonts\�����ٸ����OTF')
plt.title( '�ɷ� ������')

DG = nx.DiGraph()

DG.add_node( '�迬��')
DG.add_node( '�տ���')
DG.add_node( 'ȫ�浿')
DG.add_node( '������')

DG.add_edge('�迬��', 'ȫ�浿')
DG.add_edge('ȫ�浿', '������')
DG.add_edge('������', 'ȫ�浿')

pos=nx.spring_layout(DG)

nx.draw(DG)
nx.draw_networkx_labels(DG, pos, font_family=font_name, font_size=13)

plt.show()