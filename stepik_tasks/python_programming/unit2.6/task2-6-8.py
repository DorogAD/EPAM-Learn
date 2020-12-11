"""
https://stepik.org/lesson/3369/step/8?unit=952

Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 (число повторяется столько
раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов последовательности
должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
"""

count = int(input())
count_now = 0
i = 1
while i <= count:
    count_now += i
    if count_now < count:
        for j in range(i):
            print(i, end=' ')
        i += 1
    elif count_now == count:
        for j in range(i):
            print(i, end=' ')
        break
    else:
        diff = count - (count_now - i)
        for k in range(diff):
            print(i, end=' ')
        break
