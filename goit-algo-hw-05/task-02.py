"""
Завдання 2

Реалізувати двійковий пошук для відсортованого масиву з дробовими числами. 
Написана функція для двійкового пошуку повинна повертати кортеж, 
де першим елементом є кількість ітерацій, потрібних для знаходження елемента. 
Другим елементом має бути "верхня межа" — це найменший елемент, 
який є більшим або рівним заданому значенню.

"""

from searchers import binary_search

import random
import numpy as np


def make_test_data(num_items: int = 100):
    test_data = np.linspace(-10, 10, num_items)
    return test_data


def run_tests(num_items, to_find: int = None):
    if isinstance(num_items, list):
        test_data = num_items
    else:
        test_data = make_test_data(num_items)
    print(test_data)
    if to_find:
        sought_item = to_find
    else:
        sought_item = random.choice(test_data)
    print(f"\nItem to find: {sought_item}")
    sorted_list = sorted(test_data)
    index, iterations = binary_search(sorted_list, sought_item)
    return iterations, sorted_list[index]


target = 9.4
results = run_tests(50, target)
print(
    f"Raw result: {results}",
    f"Results type: {type(results)}",
    f"Number of iterations it took: {results[0]}",
    f"Item found: {results[1] == target}",
    f"Верхня межа пошуку (найближче значення): {results[1]}",
    sep="\n",
    end="\n" * 2,
)
