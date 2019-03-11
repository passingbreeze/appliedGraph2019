
G = nx.Graph()
G.add_edge('a', 'b', score=3)
G.add_edge('b', 'c', score=4)
G.add_edge('a', 'c', score=1)

# If we wanted a's neighbors, we just access that node directly:

print(G['a'])

# To sort those results, we use tools from the standard Python toolbox. .items() to convert the dict to a tuple and the sorted builtin to sort the results:
esort = sorted(list(G['a'].items()), key=lambda edge: edge[1]['score'])
print(esort)

