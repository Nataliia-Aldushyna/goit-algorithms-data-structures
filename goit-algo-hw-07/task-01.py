"""
Завдання 1

Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому дереві пошуку або в AVL-дереві. 
Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_max_value(root):
    if root is None:
        return None

    while root.right:
        root = root.right

    return root.value


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

max_value = find_max_value(root)
print("Найбільше значення у дереві:", max_value)
