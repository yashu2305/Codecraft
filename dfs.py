"""Depth-First Search (DFS) Sample Problem: Implement DepthFirst Search (DFS) to traverse a graph starting from a given vertex.
The graph is represented by an adjacency list"""
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set() 
    
    visited.add(start) 
    print(start) 

    for neighbor in graph[start]:
        if neighbor not in visited: 
            dfs(graph, neighbor, visited)  
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')
