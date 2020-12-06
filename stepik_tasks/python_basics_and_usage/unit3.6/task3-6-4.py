"""
https://stepik.org/lesson/24474/step/4?unit=6779

Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>



Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками,
имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

Sample Input:

<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>

Sample Output:

4 3 1
"""

from xml.etree import ElementTree

# xml = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
# root = ElementTree.fromstring(xml)
root = ElementTree.fromstring(input())

res_dict = {'count_blue': 0, 'count_red': 0, 'count_green': 0}


def counter(counter_dict, num):
    color = counter_dict['color']
    if color == 'blue':
        res_dict['count_blue'] += num
    elif color == 'red':
        res_dict['count_red'] += num
    elif color == 'green':
        res_dict['count_green'] += num


def find(child, count):
    count += 1
    counter(child.attrib, count)
    print(child.attrib)
    for sub_child in child:
        find(sub_child, count)


counter(root.attrib, 1)

for any_child in root:
    find(any_child, 1)

print(res_dict['count_red'], res_dict['count_green'], res_dict['count_blue'])
