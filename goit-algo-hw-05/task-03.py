"""
Завдання 3

Порівняти ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа 
на основі двох текстових файлів (стаття 1, стаття 2). 
Використовуючи timeit, треба виміряти час виконання кожного алгоритму для двох видів підрядків: 
одного, що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням). 
На основі отриманих даних визначити найшвидший алгоритм для кожного тексту окремо та в цілому.

"""

from searchers import *
from functools import partial

import matplotlib.pyplot as plt
import numpy as np
import timeit


def load_text(text_path: str):
    with open(text_path, "r") as file:
        text = file.read()
    return text


def run_tests_for_text(text: str, pattern: str):
    test_data = load_text(text)
    kmp = partial(kmp_search, text=test_data, pattern=pattern)
    boyer_moore = partial(boyer_moore_search, text=test_data, pattern=pattern)
    rabin_karp = partial(rabin_karp_search, text=test_data, pattern=pattern)

    kmp_time = timeit.timeit(stmt=kmp, number=20)
    boyer_moore_time = timeit.timeit(stmt=boyer_moore, number=20)
    rabin_karp_time = timeit.timeit(stmt=rabin_karp, number=20)

    print(
        f"{kmp_time} using Knuth–Morris–Pratt algorithm;",
        f"{boyer_moore_time} using Boyer-Moore algorithm;",
        f"{rabin_karp_time} using Rabin-Karp algorithm.\n",
        sep="\n",
    )

    return {
        "KMP": kmp_time,
        "Boyer-Moore": boyer_moore_time,
        "Rabin-Karp": rabin_karp_time,
    }


print("\nThe time it took to find a substring in article_1:")
success_article_1 = run_tests_for_text(
    "/Users/nataliia.aldushyna/Desktop/goit-algo-hw-05/article_1.txt",
    "поточний",
)
print(success_article_1)
print("\nThe time it took to find a substring in article_2:")
success_article_2 = run_tests_for_text(
    "/Users/nataliia.aldushyna/Desktop/goit-algo-hw-05/article_2.txt",
    "елемент",
)
print(success_article_2)
print("\nThe time it took to go through article_1 and fail to find the substring:")
fail_article_1 = run_tests_for_text(
    "/Users/nataliia.aldushyna/Desktop/goit-algo-hw-05/article_1.txt",
    "по",
)
print(fail_article_1)
print("\nThe time it took to go through article_2 and fail to find the substring:")
fail_article_2 = run_tests_for_text(
    "/Users/nataliia.aldushyna/Desktop/goit-algo-hw-05/article_2.txt",
    "елем",
)

success_values_1 = list(success_article_1.values())
success_values_2 = list(success_article_2.values())
fail_values_1 = list(fail_article_1.values())
fail_values_2 = list(fail_article_2.values())

print(success_values_1)

width = 0.2
fig = plt.subplots(figsize=(10, 6))

br1 = np.arange(3)
br2 = [x + width for x in br1]
br3 = [x + width for x in br2]
br4 = [x + width for x in br3]

plt.bar(
    br1,
    success_values_1,
    color="r",
    width=width,
    edgecolor="red",
    label="Success Article 1",
    alpha=0.7,
)
plt.bar(
    br2,
    success_values_2,
    color="g",
    width=width,
    edgecolor="green",
    label="Success Article 2",
    alpha=0.7,
)
plt.bar(
    br3,
    fail_values_1,
    color="b",
    width=width,
    edgecolor="blue",
    label="Fail Article 1",
    alpha=0.7,
)
plt.bar(
    br4,
    fail_values_2,
    color="y",
    width=width,
    edgecolor="yellow",
    label="Fail Article 2",
    alpha=0.7,
)

plt.xlabel("Algorithms", fontweight="bold", fontsize=12)
plt.ylabel("Time, seconds", fontweight="bold", fontsize=12)
plt.xticks([r + width for r in range(3)], ["KMP", "Boyer-Moore", "Rabin-Karp"])

plt.legend()
plt.show()
