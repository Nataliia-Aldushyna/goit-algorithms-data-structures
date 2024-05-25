"""
Завдання 7 - Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, 
обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. 
Для кожного кидка визначте суму чисел, які випали на обох кубиках. 
Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. 
Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, 
виявлені за допомогою методу Монте-Карло.

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, 
наведеними в таблиці вище.

"""

import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        results[total] += 1

    probabilities = {k: v / num_rolls for k, v in results.items()}
    return results, probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color="blue", alpha=0.7)
    plt.xlabel("Сума")
    plt.ylabel("Імовірність")
    plt.title("Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)")
    plt.xticks(sums)
    plt.grid(axis="y")
    plt.show()


num_rolls = 1000000  # Кількість симуляцій
results, probabilities = simulate_dice_rolls(num_rolls)

print("Сума\tЧастота\t\tІмовірність (%)")
for total in range(2, 13):
    print(f"{total}\t{results[total]}\t\t{probabilities[total]*100:.2f}")

plot_probabilities(probabilities)
