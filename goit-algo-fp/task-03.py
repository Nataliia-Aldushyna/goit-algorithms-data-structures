"""
Завдання 3 - Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, 
використовуючи бінарну купу. Завдання включає створення графа, 
використання піраміди для оптимізації вибору вершин та обчислення 
найкоротших шляхів від початкової вершини до всіх інших.

"""

import heapq
import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append((to_node, weight))

    def get_neighbors(self, node):
        return self.edges.get(node, [])

    def get_nodes(self):
        return list(self.edges.keys())


def dijkstra(graph, start_node):
    distances = {node: float("inf") for node in graph.get_nodes()}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get_neighbors(current_node):
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def visualize_heap(heap):
    G = nx.Graph()
    for i in range(len(heap)):
        G.add_node(i, label=heap[i], subset=(i + 1).bit_length())

    for i in range(len(heap)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(heap):
            G.add_edge(i, left)
        if right < len(heap):
            G.add_edge(i, right)

    pos = nx.multipartite_layout(G, subset_key="subset")
    labels = nx.get_node_attributes(G, "label")
    nx.draw(
        G,
        pos,
        with_labels=True,
        labels=labels,
        node_size=500,
        node_color="skyblue",
        font_size=10,
    )
    plt.show()


def main():
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 1)

    start_node = "A"
    distances = dijkstra(graph, start_node)
    print("Відстані від вузла", start_node)
    for node, distance in distances.items():
        print(f"Вузол {node}: {distance}")

    heap = [(distances[node], node) for node in distances]
    heapq.heapify(heap)
    visualize_heap(heap)


if __name__ == "__main__":
    main()
