
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph):
    # create directed networkx graph
    G=nx.DiGraph()

    # add edges
    G.add_edges_from(graph)

    graph_pos = nx.shell_layout(G)

    # draw nodes, edges and labels
    nx.draw_networkx_nodes(G, graph_pos, node_size=1000, node_color='blue', alpha=0.3)
    # we can now added edge thickness and edge color
    nx.draw_networkx_edges(G, graph_pos, width=2, alpha=0.3, edge_color='green')
    nx.draw_networkx_labels(G, graph_pos, font_size=12, font_family='sans-serif')

    labels = range(len(graph)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    edge_labels = dict(zip(graph, labels)) # {(23, 20): 7, (22, 23): 2, (20, 21): 10, (24, 25): 4, (21, 22): 1, (25, 20): 5, (24, 22): 8, (25, 21): 6, (23, 24): 3, (21, 24): 9}

    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels)
    # show graph
    plt.show()

# we can add more edges here as the direction is a factor now,
# edges are added as (from_node, to_node) tuples
# hence (22, 25) and (25, 22) are different. In undirected graph,
# we couldn't have told the difference.
graph = [
        (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 20),
        (25, 21), (23, 20), (24, 22), (21, 24), (20, 21)  ]


draw_graph(graph)
