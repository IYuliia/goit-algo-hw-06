import networkx as nx

G = nx.Graph()

stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
G.add_nodes_from(stations)

edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), 
         ('D', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'H')]
G.add_edges_from(edges)


def dfs(graph, start, goal):
    visited = set()
    path = []

    def dfs_helper(node):
        if node == goal:
            path.append(node)
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs_helper(neighbor):
                    path.append(node)
                    return True
        return False

    dfs_helper(start)
    path.reverse()  
    return path

def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]  
    
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []

start_station = 'A'
goal_station = 'H'

dfs_path = dfs(G, start_station, goal_station)
bfs_path = bfs(G, start_station, goal_station)

print(f"Шлях за допомогою DFS: {dfs_path}")
print(f"Шлях за допомогою BFS: {bfs_path}")
