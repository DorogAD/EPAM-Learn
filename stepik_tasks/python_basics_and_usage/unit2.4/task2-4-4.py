"""
https://stepik.org/lesson/24465/step/4?unit=6772

Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

Пример выходного файла:
ff
dde
c
ab
"""
lst = []
with open('inpt.txt') as inpt:
    for line in inpt:
        lst.append(line.strip())

new = lst[::-1]

with open('outpt.txt', 'w') as outpt:
    for line in new:
        outpt.write(line + '\n')
