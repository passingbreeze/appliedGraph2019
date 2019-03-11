import networkx as nx, matplotlib.pyplot as plt, numpy as np

def isEdge(a, b, L):
    return a!=b and np.sqrt((np.power(a[0]-b[0],2)+np.power(a[1]-b[1],2)))<=L

def main():
    g = nx.Graph()
    nodeList = {}
    with open("graph.txt", "r") as fos:
        v, length = map(int, fos.readline().split())
        for i in range(v):
            n = tuple(map(int, fos.readline().split()))
            g.add_node(i+1)
            nodeList[i+1]=n
        s,t = map(int, fos.readline().split())
    # print(v, length, s, t)
    # print(list(g.nodes))
    # print(nodeList)

    for i in range(1,len(nodeList)+1):
        for j in range(1,len(nodeList)+1):
            if isEdge(nodeList[i], nodeList[j], length):
                # print(nodeList[i], nodeList[j])
                g.add_edge(i,j)
    # print("shortest path : ", nx.shortest_path(g, source=s, target=t))

    nx.draw_networkx_nodes(g, nodeList, node_size=5)  # 그리려는 그래프의 속성을 설정해 준다
    nx.draw_networkx_edges(g, nodeList, width=1)
    nx.draw_networkx_labels(g, nodeList, font_size=10, font_family='sans-serif')

    plt.axis('on')  # 그래프 그림을 파일로 저장한다
    plt.savefig("graph.png", dpi=1000)  # 그림 파일 크기 지정
    plt.savefig("홍정민_graph.png")  # png 파일로 저장
    plt.show()
    return

if __name__ == '__main__':
    main()