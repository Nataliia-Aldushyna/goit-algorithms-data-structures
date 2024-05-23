"""
Завдання 2 - Обчислення визначеного інтеграла

Ваше друге завдання полягає в обчисленні значення інтеграла функції методом Монте-Карло.

1. Обчисліть значення інтеграла функції за допомогою методу Монте-Карло, інакше кажучи, 
знайдіть площу під цим графіком (сіра зона).
2. Перевірте правильність розрахунків, щоб підтвердити точність методу Монте-Карло, 
шляхом порівняння отриманого результату та аналітичних розрахунків 
або результату виконання функції quad. Зробіть висновки.

"""

import numpy as np
import scipy.integrate as spi


def f(x):
    return x**2


a = 0
b = 2
n = 1000000

x_rand = np.random.uniform(a, b, n)
y_rand = np.random.uniform(0, f(b), n)

points_under_curve = np.sum(y_rand <= f(x_rand))

ratio = points_under_curve / n

rectangle_area = (b - a) * f(b)

monte_carlo_integral_value = ratio * rectangle_area

quad_integral_value, _ = spi.quad(f, a, b)

print("Значення інтеграла методом Монте-Карло:", monte_carlo_integral_value)
print("Значення інтеграла за допомогою функції quad:", quad_integral_value)
