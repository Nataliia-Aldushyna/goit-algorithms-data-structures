"""
Завдання 1 - Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

- написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
- розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
- написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def merge_sorted_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return dummy.next


def merge_sort(head):
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = merge_sorted_lists(left, right)
    return sorted_list


def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def print_linked_list(head):
    while head:
        print(head.val, end=" ~ ")
        head = head.next
    print("None")


list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)

print("Список 1 до реверсування:")
print_linked_list(list1)
print("Список 2 до реверсування:")
print_linked_list(list2)

list1 = reverse_linked_list(list1)
print("Список 1 після реверсування:")
print_linked_list(list1)

list1 = merge_sort(list1)
print("Список 1 після сортування:")
print_linked_list(list1)

merged_list = merge_sorted_lists(list1, list2)
print("Результат об'єднання відсортованих списків:")
print_linked_list(merged_list)
