"""
https://stepik.org/lesson/3363/step/4?unit=1135

Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой
строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает
его среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.

Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные
значения, разделённые пробелом, последней строкой в файл с ответом.

В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой
со средними оценками по трём предметам.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
"""

students_dict = {}
with open('dataset_3363_4.txt') as f:
    for line in f:
        lst = line.strip().split(';')
        students_dict[lst[0]] = lst[1:]
        students_dict[lst[0]].append((int(lst[1]) + int(lst[2]) + int(lst[3])) / 3)


mathematics = 0
physics = 0
russian = 0
for value in students_dict.values():
    mathematics += int(value[0])
    physics += int(value[1])
    russian += int(value[2])

average_math = mathematics / len(students_dict)
average_phis = physics / len(students_dict)
average_russ = russian / len(students_dict)


with open('students.txt', 'w') as res:
    for i in students_dict:
        res.write(str(students_dict[i][3]) + '\n')
    res.write(str(average_math) + ' ')
    res.write(str(average_phis) + ' ')
    res.write(str(average_russ))
