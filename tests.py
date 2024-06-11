import networkx as nx
from rpp import rpp
from random import randint

import pytest

def test_general():
    G = nx.Graph()
    G.add_edge('A', 'B', weight=3)
    G.add_edge('B', 'C', weight=4)
    G.add_edge('C', 'D', weight=2)
    G.add_edge('D', 'A', weight=5)
    G.add_edge('A', 'C', weight=1)
    required_edges = {('A', 'B'), ('C', 'D')}

    _, min_cycle_cost = rpp(G, required_edges)
    assert min_cycle_cost == 6

def test_benchmark_5edges(benchmark):
    graphs = nx.read_graph6('testsets/ge5d1.g6')
    graph = graphs[25]
    G = nx.Graph()
    G.add_weighted_edges_from(list(e + tuple([1]) for e in graph.edges))
    benchmark(rpp, G, set())
        
def test_benchmark_10edges(benchmark):
    graphs = nx.read_graph6('testsets/ge10d1.g6')
    graph = graphs[25]
    G = nx.Graph()
    G.add_weighted_edges_from(list(e + tuple([1]) for e in graph.edges))
    benchmark(rpp, G, set())

def test_benchmark_15edges(benchmark):
    graphs = nx.read_graph6('testsets/ge15d1.g6')
    graph = graphs[25]
    G = nx.Graph()
    G.add_weighted_edges_from(list(e + tuple([1]) for e in graph.edges))
    benchmark(rpp, G, set())