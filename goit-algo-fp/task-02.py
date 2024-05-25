"""
Завдання 2 - Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала 
“дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, 
і користувач повинен мати можливість вказати рівень рекурсії.

"""

import turtle
import math


def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    return t


def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
        return

    t.forward(length)
    t.left(45)

    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)

    t.right(90)

    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)

    t.left(45)
    t.backward(length)


def main():
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Дерево Піфагора")

    t = setup_turtle()
    initial_length = 100

    draw_pythagoras_tree(t, initial_length, level)
    t.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
