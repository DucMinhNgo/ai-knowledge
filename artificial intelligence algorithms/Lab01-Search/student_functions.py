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
    # TODO: 
    
    # path=[]
    # visited={}
   
    # return visited, path
    stack = [(start, None)]
    visited = {}
    path = []

    while stack:
        current_node, parent_node = stack.pop()

        if current_node == end:
            visited[current_node] = parent_node
            break

        if current_node not in visited:
            visited[current_node] = parent_node
            path.append(current_node)

            neighbors = [neighbor for neighbor, edge_cost in enumerate(matrix[current_node]) if edge_cost > 0]

            neighbors.sort(reverse=True)

            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, current_node))

    print (visited)
    print (path)
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
    def ucs_util():
        priority_queue = [(0, start, None)]
        heapq.heapify(priority_queue)

        while priority_queue:
            cost, current_node, parent_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited[current_node] = parent_node

            if current_node == end:
                return current_node

            for neighbor, edge_cost in enumerate(matrix[current_node]):
                if edge_cost and neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor, current_node))

        return None

    visited = {}

    result_end_node = ucs_util()

    if result_end_node is not None:
        current_node = end
        path = []
        while current_node is not None:
            path.insert(0, current_node)
            current_node = visited[current_node]
    else:
        path = []


    print (visited)
    print (path)
    return visited, path

    # path=[]
    # visited={}
    # return visited, path
    

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
    print (matrix)
    # TODO:  
    # path=[]
    # visited={}
    # return visited, path
    def DFS_limit(node, depth_limit):
        """
        Depth-limited DFS helper function
        """
        if node == end:
            return True
        
        if depth_limit <= 0:
            return False
        
        visited[node] = None
        path.append(node)
        
        neighbors = [neighbor for neighbor, edge_cost in enumerate(matrix[node]) if edge_cost > 0]
        for neighbor in neighbors:
            if neighbor not in visited:
                if DFS_limit(neighbor, depth_limit - 1):
                    return True
        
        path.pop()
        return False

    path = []
    visited = {}
    depth_limit = 0

    while not DFS_limit(start, depth_limit):
        # If the goal is not reached within the current depth limit, reset and try again
        visited = {}
        path = []
        depth_limit += 1
    
    print (visited)
    print (path)

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
    # path=[]
    # visited={}
    # return visited, path
    print (matrix)
    def heuristic(node):
        return matrix[node][end]

    path = []
    visited = {}
    priority_queue = [(heuristic(start), start, None)]

    while priority_queue:
        _, current_node, parent_node = heapq.heappop(priority_queue)

        if current_node == end:
            visited[current_node] = parent_node
            path.append(current_node)
            break

        if current_node not in visited:
            visited[current_node] = parent_node
            path.append(current_node)

            neighbors = [neighbor for neighbor, edge_cost in enumerate(matrix[current_node]) if edge_cost > 0]
            neighbors.sort(key=heuristic)

            for neighbor in neighbors:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic(neighbor), neighbor, current_node))

    print (visited)
    print (path)
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
    print (matrix)
    print (pos)

    # path=[]
    # visited={}
    # return visited, path
    def heuristic(node):
        # Euclidean distance as the heuristic
        x1, y1 = pos[node]
        x2, y2 = pos[end]
        return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    path = []
    visited = {}
    priority_queue = [(0, start, None)]

    while priority_queue:
        current_cost, current_node, parent_node = heapq.heappop(priority_queue)

        if current_node == end:
            visited[current_node] = parent_node
            path.append(current_node)
            break

        if current_node not in visited:
            visited[current_node] = parent_node
            path.append(current_node)

            neighbors = [neighbor for neighbor, edge_cost in enumerate(matrix[current_node]) if edge_cost > 0]
            neighbors.sort(key=lambda neighbor: current_cost + matrix[current_node][neighbor] + heuristic(neighbor))

            for neighbor in neighbors:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (current_cost + matrix[current_node][neighbor] + heuristic(neighbor), neighbor, current_node))
    
    print (visited)
    print (path)

    return visited, path

