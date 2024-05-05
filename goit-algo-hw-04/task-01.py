"""
Завдання

Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання. 
Аналіз повинен бути підтверджений емпіричними даними, 
отриманими шляхом тестування алгоритмів на різних наборах даних. 
Емпірично перевірте теоретичні оцінки складності алгоритмів, наприклад, 
сортуванням на великих масивах. Для заміру часу виконання алгоритмів використовуйте модуль timeit.


Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим,
і саме з цієї причини програмісти, в більшості випадків, використовують вбудовані в Python алгоритми, 
а не кодують самі. 
Зробіть висновки.

"""

import random
import timeit


def generate_random_list(size):
    return [random.randint(0, 1000) for _ in range(size)]


def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


data_sizes = [1000, 5000, 10000]
for size in data_sizes:
    data = generate_random_list(size)

    merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
    timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)

    print(f"Data size: {size}")
    print(f"Merge Sort time: {merge_sort_time}")
    print(f"Insertion Sort time: {insertion_sort_time}")
    print(f"Timsort time: {timsort_time}")
    print()
