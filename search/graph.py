import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

            
    def bfs(self, start, end=None):
        
        if len(self.graph) == 0:
            raise ValueError("Empty graph")

        if start not in self.graph:
            raise ValueError("Start node not in graph")
        
        if end is not None and end not in self.graph:
            raise ValueError(f"End node '{end}' not in graph")
        

        queue = [[start]] # here we make a list of lists, where each list is a path
        visited = {} # use dict for traversal order, O(1) lookup
        visited[start] = True

        while queue:
            path = queue.pop(0) # on each queue pop, we remove the most recent path (list)
            node = path[-1] # BUT we only explore the neighbors of the last node in the path (frontier node)

            # We keep track of path so we can return it if it contains the end node, but at the same time
            # we update the visited node set for the full BDS traversal order
            if node not in visited:
                visited.append(node)

            if end is not None and node == end:
                return path

            # Explore neighbors
            for neighbor in sorted(self.graph[node]): #make it sorted to allow for networkx assertion
                if neighbor not in visited: #this is O(1), for dict
                    visited[neighbor] = True
                    new_path = path + [neighbor] # append the neighbor to the path
                    queue.append(new_path) # now the new path, with the new neighbor is added to the queue
                    # for each neighbor we add a new path to the queue, this is so that we can return if we reach the end node
                    # may seem redundant, but we only explore the neighbors of the last node in the path

        # No end node: return full traversal
        if end is None:
            return list(visited.keys())
        
        # End node specified but no path found, full traversal and queue empty
        return None

























