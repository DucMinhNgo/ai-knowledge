import numpy as np
from collections import deque
from queue import PriorityQueue
import heapq

def BFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO:   
    path=[]
    visited={}
    queue = deque([start])
    visited[start] = None
    print (start)
    print (end)
    print (queue)
    print (matrix)
    print (matrix[0])
    print (np.nonzero(matrix[0])[0])

    while queue:
        print (queue)
        current_node = queue.popleft()
        print (current_node)

        if current_node == end:
            print ('END')
            # Reconstruct the path from end to start
            while current_node is not None:
                print ('current_mode: ', current_node)
                path.insert(0, current_node)
                current_node = visited[current_node]
            break

        neighbors = np.nonzero(matrix[current_node])[0]
        print ('neighbors:', neighbors)

        for neighbor in neighbors:
            if neighbor not in visited:
                visited[neighbor] = current_node
                queue.append(neighbor)
    print (visited)
    print (path)

    return visited, path

def DFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    def dfs_recursive(current_node, visited, path):
        """
        Recursive helper function for DFS
        """
        # Mark the current node as visited
        visited[current_node] = True

        # Append the current node to the path
        path.append(current_node)

        # Check if the current node is the end node
        if current_node == end:
            return True

        # Find all adjacent nodes of the current node
        neighbors = np.nonzero(matrix[current_node])[0]

        # Explore unvisited neighbors
        for neighbor in neighbors:
            if neighbor not in visited:
                # Recursively call DFS for unvisited neighbors
                if dfs_recursive(neighbor, visited, path):
                    return True

        # If the end node is not found in the current path, backtrack
        path.pop()
        return False

    # TODO: 
    
    path=[]
    visited={}

    dfs_recursive(start, visited, path)
   
    return visited, path


def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
    Parameters:
    ---------------------------
    matrix: np array
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:  
    priority_queue = [(0, start)]
    path=[]
    visited={}
     # UCS algorithm
    while priority_queue:
        # Dequeue a node with the lowest cost
        current_cost, current_node = heapq.heappop(priority_queue)

        # Check if the current node is the end node
        if current_node == end:
            # Reconstruct the path from end to start
            while current_node is not None:
                path.insert(0, current_node)
                current_node = visited[current_node]
            break

        # Find all adjacent nodes of the current node
        neighbors = np.nonzero(matrix[current_node])[0]

        # Explore unvisited neighbors
        for neighbor in neighbors:
            # Calculate the cost to reach the neighbor
            neighbor_cost = current_cost + matrix[current_node, neighbor]

            # Enqueue the neighbor if not visited or with a lower cost
            if neighbor not in visited or neighbor_cost < visited[neighbor][0]:
                visited[neighbor] = (neighbor_cost, current_node)
                heapq.heappush(priority_queue, (neighbor_cost, neighbor))
    return visited, path
    

def IDS(matrix, start, end):
    """
    Iterative deepening search algorithm
    Parameters:
    ---------------------------
    matrix: np array
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:  
    path=[]
    visited={}
    return visited, path

def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm 
    heuristic : edge weights
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    return visited, path

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
    heuristic: eclid distance based positions parameter
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 

    path=[]
    visited={}
    return visited, path

