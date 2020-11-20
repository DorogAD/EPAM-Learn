'''
https://stepik.org/lesson/3378/step/3?unit=961

Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.
'''
import requests

def link(url):
    r = requests.get(url)
    #print(r)
    l = r.text.splitlines()
    #print(l)
    w = l[0].split()
    if w[0] == 'We':
        print(r.text)
    else:
        link('https://stepic.org/media/attachments/course67/3.6.3/' + r.text.strip())

link('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')


