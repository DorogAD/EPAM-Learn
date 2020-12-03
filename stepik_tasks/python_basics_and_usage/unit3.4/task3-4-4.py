"""
https://stepik.org/lesson/24473/step/4?unit=6777


Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть
поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass


Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется
явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:

A : 3
B : 1
C : 2
"""
import json

# js = json.loads('[{"name": "DH", "parents": ["D", "BF", "DE", "AE"]}, {"name": "D", "parents": ["AE"]}, {"name": "B", "parents": []}, {"name": "AE", "parents": ["F"]}, {"name": "BG", "parents": ["H", "CH"]}, {"name": "H", "parents": []}, {"name": "E", "parents": ["CG", "B"]}, {"name": "BH", "parents": ["CG"]}, {"name": "CE", "parents": []}, {"name": "CH", "parents": ["E"]}, {"name": "C", "parents": ["CE"]}, {"name": "A", "parents": []}, {"name": "DE", "parents": ["BH"]}, {"name": "F", "parents": []}, {"name": "CG", "parents": ["C", "G"]}, {"name": "G", "parents": []}, {"name": "BF", "parents": ["F"]}]')
# js = json.loads('[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]')
# js = json.loads('[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]')
js = json.loads(input())

new_dict = {}


def dict_work(one_key, one_value):
    one_value = list(set(one_value))
    if one_key in new_dict:
        new_dict[one_key] += one_value
    else:
        new_dict[one_key] = one_value


for note in js:
    child_list = []
    parent = note["name"]
    child_list.append(note["name"])
    dict_work(parent, child_list)
    for parent in note["parents"]:
        child_list.append(note["name"])
        dict_work(parent, child_list)

result_dict = {}


def find(element):
    global children
    for any_child in new_dict[element]:
        if any_child not in children:
            children.append(any_child)
            find(any_child)


for parent in new_dict:
    children = []
    for ch in new_dict[parent]:
        if ch not in children:
            children.append(ch)
            find(ch)
    result_dict[parent] = children


list_keys = list(result_dict.keys())
list_keys.sort()
for key in list_keys:
    print(key, ':', len(result_dict[key]))
