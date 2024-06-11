import networkx as nx
from rpp import rpp

G = nx.Graph()
G.add_edge('A', 'B', weight=3)
G.add_edge('B', 'C', weight=4)
G.add_edge('C', 'D', weight=2)
G.add_edge('D', 'A', weight=5)
G.add_edge('A', 'C', weight=1)

required_edges = {('A', 'B'), ('C', 'D')}

optimal_cycle, min_cycle_cost = rpp(G, required_edges)
print("RPP cycle:", optimal_cycle)
print("RPP cycle cost:", min_cycle_cost)
