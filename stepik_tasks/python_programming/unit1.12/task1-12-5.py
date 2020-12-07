"""
https://stepik.org/lesson/5047/step/5?unit=1086

Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль
в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
"""
a = int(input())
b = int(input())
c = int(input())

max_num = 0
mid_num = 0
min_num = 0

if a >= b and a >= c:
    max_num = a
    if b >= c:
        mid_num = b
        min_num = c
    elif b < c:
        mid_num = c
        min_num = b
elif b >= a and b >= c:
    max_num = b
    if a >= c:
        mid_num = a
        min_num = c
    elif a < c:
        mid_num = c
        min_num = a
elif c >= a and c >= b:
    max_num = c
    if a >= b:
        mid_num = a
        min_num = b
    elif a < b:
        mid_num = b
        min_num = a
else:
    print('Wrong input!')

print(max_num)
print(min_num)
print(mid_num)
