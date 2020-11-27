"""
https://stepik.org/lesson/24471/step/7?unit=6780

Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... >
и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов,
которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть,
за исключением случаев с относительными ссылками вида <a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.
"""

import re
import requests

result = []

link = input()
# link = 'http://pastebin.com/raw/7543p0ns'

content = requests.get(link).text

link_list = re.findall(r'(<a.*href=[\'"])(\w+://)?(\w[a-zA0-9.-]+)', content)

for site in link_list:
    result.append(site[2])

final = sorted(list(set(result)))

for i in final:
    print(i)
