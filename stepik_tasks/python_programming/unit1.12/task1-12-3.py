"""
https://stepik.org/lesson/5047/step/3?unit=1086

Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число,
второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число")
и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
"""

num1 = float(input())
num2 = float(input())
operation = str(input())

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '/':
    if num2 == 0:
        print('Деление на 0!')
    else:
        print(num1 / num2)
elif operation == '*':
    print(num1 * num2)
elif operation == 'mod':
    if num2 == 0:
        print('Деление на 0!')
    else:
        print(num1 % num2)
elif operation == 'pow':
    print(pow(num1, num2))
elif operation == 'div':
    if num2 == 0:
        print('Деление на 0!')
    else:
        print(num1 // num2)
