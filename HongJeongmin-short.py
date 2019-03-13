import networkx as nx, matplotlib.pyplot as plt, numpy as np

def isEdge(a, b, L):
    return (np.sqrt((np.power(a[0]-b[0],2)+np.power(a[1]-b[1],2)))<=L)

def main():
    g = nx.Graph()
    nodeList = {}
    eList = []
    with open("graph.txt", "r") as fos:
        v, length = map(int, fos.readline().split())
        for i in range(v):
            n = tuple(map(int, fos.readline().split()))
            nodeList[i+1]=n
        s,t = map(int, fos.readline().split())
    print(nodeList)
    for i in range(1,len(nodeList)+1):
        for j in range(1,len(nodeList)+1):
            if nodeList[i]!=nodeList[j] and isEdge(nodeList[i], nodeList[j], length):
                eList.append((i,j))

    g.add_nodes_from(nodeList.keys())
    g.add_edges_from(eList)

    nx.draw_networkx_nodes(g, nodeList, node_size=50, label=True, node_color='black')  # 그리려는 그래프의 속성을 설정해 준다
    nx.draw_networkx_edges(g, nodeList, edgelist=eList, width=2, edge_color='gray')
    nx.draw_networkx_labels(g, nodeList, font_size=5, font_color='white', font_family='sans-serif')

    try:
        spNode = nx.algorithms.shortest_path(g, source=s, target=t)
        spEdge = [(spNode[i], spNode[i+1]) for i in range(len(spNode)-1)]
        nx.draw_networkx_edges(g, nodeList, edgelist=spEdge, width=3, edge_color='red')
        title = "Red line is the shortest path between {} and {}.".format(s,t)
    except nx.NodeNotFound :
        title = "There is no shortest path between {} and {}.".format(s,t)

    plt.title(title)
    plt.xlim([0,100])
    plt.ylim([0,100])
    plt.xticks([0,50,100])
    plt.yticks([0,50,100])
    plt.axis('on')  # 그래프 그림을 파일로 저장한다
    plt.savefig("HongJeongmin_graph.png", dpi=1000)  # 그림 파일 크기 지정
    plt.show()
    return

if __name__ == '__main__':
    main()