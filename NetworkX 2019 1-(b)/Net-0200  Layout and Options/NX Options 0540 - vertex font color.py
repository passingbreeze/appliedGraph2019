
# https://python-graph-gallery.com/all-charts/


import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Build a dataframe with your connections
df = pd.DataFrame({ 'from':['A', 'B', 'C','A'], 'to':['D', 'A', 'E','C']})

# Build your graph
G=nx.from_pandas_dataframe(df, 'from', 'to')

# Custom the edges:
nx.draw(G, with_labels=True, node_size=1000, \
        font_size=25, font_color="black", font_weight="bold")


plt.show( )
