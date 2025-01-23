# Assignment 2
Breadth-first search

## Coding Assessment
In search/graph.py:
* Define the function bfs that takes in a graph, start node, and optional node and:
	* If no end node is provided, returns a list of nodes in order of breadth-first search traversal from the given start node
	* If an end node is provided and a path exists, returns a list of nodes in order of the shortest path to the end node
	* If an end node is provided and a path does not exist, returns None
* Be sure that your code can handle possible edge cases, e.g.:
	* running bfs traversal on an empty graph
	* running bfs traversal on an unconnected graph
	* running bfs from a start node that does not exist in the graph
	* running bfs search for an end node that does not exist in the graph
	* any other edge cases you can think of 

In test/test_bfs.py:
* Write unit tests for breadth-first traversal and breadth-first search 
* You may use the two networks provided in the data folder or create your own for testing
* Test at least 2 possible edge cases (listed above)
* Include a test case that fails and raises an exception


## Software Development Assessment

### Overview
This project implements a custom Graph class with Breadth-First Search (BFS) functionality using NetworkX for graph representation.


### Key Components
- `Graph` class: Manages graph operations
- BFS implementation with:
  - Ordered traversal
  - Efficient node lookup
  - Path finding
  - Error handling

### Implementation  Specifics
- Ordered boolean dictionary for visited
- List of lists for queue, to return shortest path


### Edge Cases Handled
- Empty graph
- Non-existent nodes
- Unconnected nodes

### Requirements
- Python 3.7+
- NetworkX library

### Running Tests
```bash
pytest test/test_bfs.py
```

### Example Usage
```python
# Create graph from adjacency list
graph = Graph(filename='network.adjlist')

# Perform full BFS traversal
traversal = graph.bfs(start='StartNode')

# Find path between nodes
path = graph.bfs(start='StartNode', end='EndNode')
```

# Reference Information
## Test Data
Two networks have been provided in an adjacency list format readable by [networkx](https://networkx.org/), is a commonly used python package for working with graph structures. These networks consist of two types of nodes:
* Faculty nodes 
* Pubmed ID nodes

However, since these are both stored as strings, you can treat them as equivalent nodes when traversing the graph. The first graph ("citation_network.adjlist") has nodes consisting of all BMI faculty members, the top 100 Pubmed papers *cited by* faculty, and the top 100 papers that *cite* faculty publications. Edges are directed and and edge from node A -> B indicates that node A *is cited by* node B. There are 5120 nodes and 9247 edges in this network.

The second network is a subgraph of the first, consisting of only the nodes and edges along the paths between a small subset of faculty. There are 30 nodes and 64 edges.


# Grading

## Code (6 points)
* Breadth-first traversal works correctly (3)
* Traces the path from one faculty to another (2)
* Handles edge cases (1)

## Unit tests (3 points)
* Output traversal for mini data set (1)
* Tests for at least two possible edge cases (1)
* Correctly uses exceptions (1)

## Style (1 points)
* Readable code with clear comments and method descriptions
* Updated README with description of your methods

