"""
Завдання 5 - Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, 
яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, 
використовуючи 16-систему RGB (приклад #1296F0). 
Кольори вузлів мають змінюватися від темних до світлих відтінків, 
залежно від послідовності обходу. Кожен вузол при його відвідуванні 
має отримувати унікальний колір, який візуально відображає порядок обходу.

"""

import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = None
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [
        node[1]["color"]
        for node in tree.nodes(data=True)
        if node[1]["color"] is not None
    ]
    labels = {
        node[0]: node[1]["label"]
        for node in tree.nodes(data=True)
        if node[1]["color"] is not None
    }

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def dfs(node, visited=set(), hue=0):
    if node is None:
        return
    visited.add(node)
    color = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(hue / 360, 1, 1))
    node.color = f"#{color[0]:02X}{color[1]:02X}{color[2]:02X}"  # Представлення кольору у форматі RGB
    hue += 25  # Збільшення відтінка для наступного вузла
    if node.left not in visited:
        dfs(node.left, visited, hue)
    if node.right not in visited:
        dfs(node.right, visited, hue)


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

dfs(root)
draw_tree(root)
