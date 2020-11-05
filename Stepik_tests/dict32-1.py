q = {'a': [5], 'b': 7, 'c': 27, 'd': 44}
q['a'].append(25)# => q = {'a': [5, 25], 'b': 7, 'c': 27, 'd': 44}

'''
Напишите функцию update_dictionary(d, key, value), которая принимает на 
вход словарь d и два числа: key и value.

Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2∗key. 
Если и ключа 2∗key нет, то нужно добавить ключ 2∗key в словарь и сопоставить ему список 
из переданного элемента [value].

Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функции input и print.
'''

def update_dictionary(d, key, value):
    key2 = 2 * key
    if key in d:
        d[key].append(value)
    elif key2 in d:
        d[key2].append(value)
    else:
        d[key2] = [value]
    return d

#x = update_dictionary({}, 1, 25)
x = update_dictionary({2: [25]}, 2, 18)
print(x)