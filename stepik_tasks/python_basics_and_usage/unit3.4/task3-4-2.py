"""
https://stepik.org/lesson/24473/step/2?unit=6777

Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по
настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
https://stepik.org/media/attachments/lesson/24473/Crimes.csv
"""
import csv

list_2015 = []

with open('crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if '2015' in row[2]:
            list_2015.append(row)

primary_types = []

for crime in list_2015:
    primary_types.append(crime[5])

max_elem = ''
max_count = 0

for element in primary_types:
    if primary_types.count(element) > max_count:
        max_elem = element
        max_count = primary_types.count(element)

print(max_elem)
