"""
https://stepik.org/lesson/24471/step/6?unit=6780

Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">,
возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за
один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.
"""
import re
import requests

# url_a = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
# url_b = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
url_a = input(str())
url_b = input(str())

content_a = requests.get(url_a).text

first_transit = []
second_transit = []

first_transit += re.findall('<a href="?\'?([^"\'>]*)', content_a)


for every_href in first_transit:
    content_c = requests.get(every_href).text
    second_transit += re.findall('<a href="?\'?([^"\'>]*)', content_c)
if url_b in second_transit:
    print('Yes')
else:
    print('No')
