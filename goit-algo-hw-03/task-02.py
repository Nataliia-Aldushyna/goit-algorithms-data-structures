"""
Завдання 2

Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, 
що користувач повинен мати можливість вказати рівень рекурсії.

"""

import turtle


def draw_koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            draw_koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def main():
    order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    snowflake = turtle.Turtle()
    snowflake.speed(0)

    snowflake.penup()
    snowflake.goto(-150, 90)
    snowflake.pendown()
    snowflake.color("aqua")

    for _ in range(3):
        draw_koch_snowflake(snowflake, order, 300)
        snowflake.right(120)

    window.mainloop()


if __name__ == "__main__":
    main()
