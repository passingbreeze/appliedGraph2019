
import networkx as nx
import numpy
import matplotlib.pyplot as plt

numpy.random.seed(1114)

def draw_graph(graph):
    # graph 객체에서 노드들을 뽑아 nodes 에 저장한다
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])
    print(nodes)

    G=nx.Graph()   # 그래프 객체를 하나 만든다
    for node in nodes:  # add_node() 를 통해 그래프에 노드를 입력한다
        G.add_node(node)

    for edge in graph:  # add_edges() 를 통해 노드간의 엣지를 지정해 준다
        G.add_edge(edge[0], edge[1])

    pos = nx.spring_layout(G)     # 위치를 지정한다.
    nx.draw(G, pos)

    # 그리려는 그래프의 속성을 설정해 준다
    nx.draw_networkx_nodes(G,pos,node_size=22)
    nx.draw_networkx_edges(G,pos,width=1)
    nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')

    # 그래프 그림을 파일로 저장한다
    plt.axis('on')
    plt.savefig("graph1000.png", dpi=1000) # 그림 파일 크기 지정
    plt.savefig("wgraph.png") # png 파일로 저장

    plt.show()

# 그리고자 하는 그래프 예제
graph = [(20, 21),(21, 23),(24, 25), (23, 24),(24, 22), (25, 20), (23,20)]
draw_graph(graph)

