"""
Завдання 2

Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, 
який було розроблено у першому завданні.

Далі порівняйте результати виконання обох алгоритмів для цього графа, 
висвітлить різницю в отриманих шляхах. 
Поясніть, чому шляхи для алгоритмів саме такі.

"""

import networkx as nx

G = nx.Graph()
G.add_nodes_from(["Вузол 1", "Вузол 2", "Вузол 3", "Вузол 4", "Вузол 5"])
G.add_edges_from(
    [
        ("Вузол 1", "Вузол 2"),
        ("Вузол 1", "Вузол 3"),
        ("Вузол 2", "Вузол 3"),
        ("Вузол 2", "Вузол 4"),
        ("Вузол 3", "Вузол 4"),
        ("Вузол 4", "Вузол 5"),
    ]
)


def dfs_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_node(start):
        return []
    paths = []
    for node in graph.neighbors(start):
        if node not in path:
            new_paths = dfs_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    paths = []
    while queue:
        (node, path) = queue.pop(0)
        for next_node in graph.neighbors(node):
            if next_node not in path:
                if next_node == end:
                    paths.append(path + [next_node])
                else:
                    queue.append((next_node, path + [next_node]))
    return paths


start_node = "Вузол 1"
end_node = "Вузол 5"
dfs_result = dfs_paths(G, start_node, end_node)
bfs_result = bfs_paths(G, start_node, end_node)

print("Шляхи за допомогою DFS:", dfs_result)
print("Шляхи за допомогою BFS:", bfs_result)
