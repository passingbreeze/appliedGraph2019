import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx
import os
import numpy as np
np.random.seed(1)

def read_input_file(file_name):
    f = open(file_name)
    f_lines = f.readlines()
    N,L, START, END = 0, 0, 0, 0
    node_pos = {}
    idx = 1
    for i, line in enumerate(f_lines):
        line = line.split()
        if i == 0 :
            N, L = line[0], line[1]
        elif i == len(f_lines)-1:
            START, END = line[0], line[1]
        else:
            node_pos[idx] = np.array([line[0], line[1]],dtype=int)
            idx += 1
            
    N,L,START,END = int(N),int(L),int(START),int(END)
    
    return N,L,START,END,node_pos
    

if __name__ == "__main__":
    
    # Read Graph data file
    N,L,START,END,pos = read_input_file("graph.txt")
    
    # Get Edges
    edges = []
    for i in range(N):
        for j in range(i+1):
            (x1,y1) = pos[i+1]
            (x2,y2) = pos[j+1]
            dist = np.sqrt((x1-x2)**2 + (y1-y2)**2)
            if dist <= L: 
                edges.append((i+1,j+1))
                
    # Draw Graph
    plt.figure(figsize=(7, 7))
    G = nx.Graph()
    nodes = np.array(range(len(pos)))+1

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    nx.draw_networkx_nodes(G, pos, node_size=700,alpha=1,node_color='black')
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=6, edge_color='black', alpha=0.2 ,style='dashed')
    nx.draw_networkx_labels(G, pos, font_size=15, font_family='sans-serif',alpha=1,font_color='white')

    try:
        # Calculate shortest path using NetworkX algorithm
        path = nx.algorithms.shortest_path(G=G, source=START, target=END)
        path_edges = [(path[i],path[i+1]) for i in range(len(path)-1)]
        # Draw path
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=6, edge_color='red', alpha=1)
        title = "Shortest Path Between ({} , {})".format(START,END)
    except:
        title = "Shortest Path Between ({} , {}) not exist".format(START,END)
        print("Shortest path not exist!")

    plt.title(title)
    plt.axis("on")
    plt.savefig("LeeKwangho_graph.png")
    