# write tests for bfs
import pytest
import networkx as nx
from search import graph


def test_bfs_traversal():
    """ 
    Tests traversal order == netowrkx bfs tree
    """
    tiny_network = graph.Graph(filename='./data/tiny_network.adjlist')
    traversal = tiny_network.bfs(start='Luke Gilbert')
    nx_tree = nx.bfs_tree(tiny_network.graph, source='Luke Gilbert',sort_neighbors=sorted)
    nx_traversal = list(nx_tree.nodes)
    assert traversal == nx_traversal


def test_bfs():

    """
    Tests shortest path
    """
    tiny_network = graph.Graph(filename='./data/tiny_network.adjlist')
    path = tiny_network.bfs(start='Luke Gilbert', end='Hani Goodarzi')
    assert path == nx.shortest_path(tiny_network.graph,source='Luke Gilbert',target='Hani Goodarzi')

    # End node does not exist
    with pytest.raises(ValueError):
        tiny_network.bfs(start='Luke Gilbert',end="non_existent_node")
    
    # Start node does not exist
    with pytest.raises(ValueError):
        tiny_network.bfs(start='non_existent_node',end="Hani Goodarzi")
    


def test_bfs_edge_cases():
    empty_graph = graph.Graph(filename='./data/empty_graph.adjlist')
    with pytest.raises(ValueError):
        empty_graph.bfs(start='Luke Gilbert')
