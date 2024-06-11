import networkx as nx
import itertools

def rpp(graph, required_edges):
    weights = nx.get_edge_attributes(graph, 'weight')
    # Поиск всех компонент связности в графе
    components = list(nx.connected_components(graph))
    num_components = len(components)
    
    # Цикл для перебора всех возможных подмножеств рёбер T
    min_cycle_cost = float('inf')
    optimal_cycle = None
    for component in components:
        for T in itertools.combinations(component, num_components-1):
            G = graph.copy()
            G.add_edges_from(T)
            
            # Поиск паросочетания на вершинах нечётной степени
            odd_degree_nodes = [node for node in G.nodes() if G.degree(node) % 2 != 0]
            odd_degree_subgraph = G.subgraph(odd_degree_nodes)
            matching = nx.max_weight_matching(odd_degree_subgraph, weight='weight')
            
            # Построение цикла, содержащего все рёбра из R и T
            cycle_edges = required_edges.union(set(T)).union(set(matching))
            cycle_cost = 0
            for edge in cycle_edges:
                if edge in weights:
                    cycle_cost += weights[edge]
                else:
                    cycle_cost += weights[(edge[1], edge[0])]
            
            # Обновление оптимального цикла
            if cycle_cost < min_cycle_cost:
                min_cycle_cost = cycle_cost
                optimal_cycle = cycle_edges
    
    return optimal_cycle, min_cycle_cost
