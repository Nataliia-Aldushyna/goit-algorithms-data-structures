"""
Завдання

Уявіть, що вам на технічному інтерв'ю дають наступну задачу, яку треба розв'язати за допомогою купи.
Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, 
використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. 
Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, 
а загальні витрати дорівнюють сумі з'єднання всіх кабелів.

Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

"""

import heapq


def min_cost_to_connect_cables(cables):
    if not cables:
        return 0
    if len(cables) == 1:
        return cables[0]

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost


cables = [8, 4, 6, 12]
print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(cables)) 
