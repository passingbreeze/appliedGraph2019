

import networkx as nx
import matplotlib.pyplot as plt
import numpy

G = nx.petersen_graph()

options = {
  'node_color': 'black',
  'node_size': 100,
  'width': 3,
}
plt.subplot(231)  # 2 by 2에서 1
nx.draw_random(G, **options)

plt.subplot(232)
nx.draw_circular(G, **options)

plt.subplot(233)
nx.draw_spectral(G, **options)

plt.subplot(234)
nx.draw_shell(G, nlist=[range(5,10), range(5)], **options)

plt.show()
