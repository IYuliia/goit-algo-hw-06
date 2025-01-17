import heapq

def dijkstra(graph, start):
    
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    previous_vertices = {vertex: None for vertex in graph}

    queue = [(0, start)] 

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_vertices

def get_shortest_path(previous_vertices, start, end):
    path = []
    current_vertex = end

    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]

    return path[::-1]  

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 3, 'E': 1},
    'D': {'B': 2, 'F': 1},
    'E': {'C': 1, 'F': 4},
    'F': {'D': 1, 'E': 4, 'G': 2},
    'G': {'F': 2, 'H': 3},
    'H': {'G': 3}
}

start = 'A'
end = 'H'

distances, previous_vertices = dijkstra(graph, start)
shortest_path = get_shortest_path(previous_vertices, start, end)

print("Найкоротші відстані від вершини", start, "до всіх інших вершин:")
print(distances)

print("\nНайкоротший шлях від", start, "до", end, ":")
print(shortest_path)
