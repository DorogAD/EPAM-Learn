'''
https://stepik.org/lesson/24466/step/5?unit=6773

В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента
исходной даты date пройдет число дней, равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta для прибавления дней к дате.
'''

from datetime import datetime, timedelta

y, m, d = input().split()
y, m, d = int(y), int(m), int(d)
day = int(input())
date = datetime(y, m, d)
new = date + timedelta(day)
print(new.year, end=' ')
print(new.month, end=' ')
print(new.day, end=' ')
