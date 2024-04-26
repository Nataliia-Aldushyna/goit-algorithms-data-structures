"""
Завдання 2
Необхідно розробити функцію, яка приймає рядок як вхідний параметр, 
додає всі його символи до двосторонньої черги (deque з модуля collections в Python), 
а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 
Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, 
а також бути нечутливою до регістру та пробілів.

"""

from collections import deque


def is_palindrome(s):
    s = s.lower().replace(" ", "")
    char_queue = deque(s)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True


print(is_palindrome("radar"))  # True
print(is_palindrome("level"))  # True
print(is_palindrome("noon"))  # True
print(is_palindrome("hello"))  # False

print(is_palindrome("Анна"))  # True
print(is_palindrome("дід"))  # True
print(is_palindrome("шалаш"))  # True
print(is_palindrome("привіт"))  # False
