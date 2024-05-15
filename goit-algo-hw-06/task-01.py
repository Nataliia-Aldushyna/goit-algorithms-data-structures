"""
Завдання 1

Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі 
(наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).
Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, 
кількість вершин та ребер, ступінь вершин).

"""

import networkx as nx
import matplotlib.pyplot as plt

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

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1500, font_size=10)
plt.title("Візуалізація графа")
plt.show()

print("Кількість вершин у графі:", G.number_of_nodes())
print("Кількість ребер у графі:", G.number_of_edges())

degrees = dict(G.degree())
for node in G.nodes():
    print(f"Ступінь вершини {node}: {degrees[node]}")
