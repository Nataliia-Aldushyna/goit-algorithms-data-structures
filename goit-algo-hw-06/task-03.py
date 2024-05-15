"""
Завдання 3

Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: 
додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.

"""

import networkx as nx

G = nx.Graph()
G.add_nodes_from(["Вузол 1", "Вузол 2", "Вузол 3", "Вузол 4", "Вузол 5"])
G.add_weighted_edges_from(
    [
        ("Вузол 1", "Вузол 2", 1),
        ("Вузол 1", "Вузол 3", 2),
        ("Вузол 2", "Вузол 3", 2),
        ("Вузол 2", "Вузол 4", 1),
        ("Вузол 3", "Вузол 4", 3),
        ("Вузол 4", "Вузол 5", 2),
    ]
)

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph.nodes()}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph.nodes()):
        current_node = min(
            (node for node in graph.nodes() if node not in visited),
            key=lambda node: distances[node],
        )
        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                distance_to_neighbor = (
                    distances[current_node] + graph[current_node][neighbor]["weight"]
                )
                if distance_to_neighbor < distances[neighbor]:
                    distances[neighbor] = distance_to_neighbor

    return distances

shortest_paths = {}
for node in G.nodes():
    shortest_paths[node] = dijkstra(G, node)

for node in shortest_paths:
    print(f"Найкоротші шляхи від вершини {node}: {shortest_paths[node]}")
