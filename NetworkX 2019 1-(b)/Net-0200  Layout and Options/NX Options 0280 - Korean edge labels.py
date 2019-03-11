

import networkx as nx
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/NanumMyeongjo.ttf").get_name()
plt.rc('font', family=font_name)


G=nx.Graph()

a=u"오달수"
b="polarity"
c="alpha"
d="beta"
G.add_edge(a,b,weight=0.5)
G.add_edge(b,c,weight=0.5)
G.add_edge(c,d,weight=0.5)
G.add_edge(a,d,weight=0.5)
G.add_edge(a,c,weight=0.5)
G.add_edge(b,d,weight=0.5)

pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=1000, node_color="lightblue")

# edges
nx.draw_networkx_edges(G,pos, width=2,alpha=0.5,edge_color='green')

# labels
nx.draw_networkx_labels(G,pos,font_size=20,font_family=font_name)

nx.draw_networkx_edge_labels(G,pos,
    {
        (a,b):u"뭐여", (b,c): u"바나나", (c,d):"w", (a,d):"z", (a,c):"v", (b,d):"r"
    }, font_family=font_name, font_size=20, label_pos=0.3

)

plt.axis('off')
plt.title( u'TITLE: 이것은 제목줄입니다.' )
plt.show() # display