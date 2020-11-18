'''
https://stepik.org/lesson/3372/step/9?unit=955

Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
удаляет из него все нечётные значения, а чётные нацело делит на два.
'''

def modify_list(l):
    new = []
    for i in l:
        if i % 2 == 0:
            new.append(int(i / 2))
    l.clear()
    for j in new:
        l.append(j)


lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
print(lst)

