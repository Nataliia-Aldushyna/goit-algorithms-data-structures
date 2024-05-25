"""
Завдання 6 - Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — 
жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі 
вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. 
Дані про їжу представлені у вигляді словника, де ключ — назва страви, 
а значення — це словник з вартістю та калорійністю.

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, 
максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, 
яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.

"""

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            chosen_items.append(item)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return chosen_items, total_calories


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name = item_names[i - 1]
        item_cost = items[item_name]["cost"]
        item_calories = items[item_name]["calories"]
        for w in range(1, budget + 1):
            if item_cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_cost] + item_calories)
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name = item_names[i - 1]
            chosen_items.append(item_name)
            w -= items[item_name]["cost"]

    return chosen_items, total_calories


budget = 100
print("Greedy Algorithm:")
chosen_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Chosen items:", chosen_items_greedy)
print("Total calories:", total_calories_greedy)

print("\nDynamic Programming:")
chosen_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("Chosen items:", chosen_items_dp)
print("Total calories:", total_calories_dp)
