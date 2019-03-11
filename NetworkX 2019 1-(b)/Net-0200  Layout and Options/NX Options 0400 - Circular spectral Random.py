

import pylab as plt #import Matplotlibplotting interface

g = nx.watts_strogatz_graph(50, 8, 0.1)
nx.draw(g)
plt.show( )

nx.draw_random(g)
plt.show( )

nx.draw_circular(g)
plt.show( )

nx.draw_spectral(g)


#plt.savefig('graph.png')
plt.show( )