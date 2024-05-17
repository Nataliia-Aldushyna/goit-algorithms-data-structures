"""
Завдання 3

Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві. 
Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_sum(root):
    if root is None:
        return 0

    return root.value + tree_sum(root.left) + tree_sum(root.right)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

total_sum = tree_sum(root)
print("Сума всіх значень у дереві:", total_sum)
