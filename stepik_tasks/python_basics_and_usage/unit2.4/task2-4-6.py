"""
https://stepik.org/lesson/24465/step/6?unit=6772

Вам дана в архиве (https://stepik.org/media/attachments/lesson/24465/main.zip) файловая структура,
состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

Для лучшего понимания формата задачи, ознакомьтесь с примером.
Пример архива https://stepik.org/media/attachments/lesson/24465/sample.zip
Пример ответа https://stepik.org/media/attachments/lesson/24465/sample_ans.txt
"""

import os.path

lst = []

os.chdir('test')
for cur_dir, dirs, files in os.walk('.'):
    for i in files:
        if i[-3:] == '.py':
            lst.append(cur_dir.strip('.\\'))


lst = list(set(lst))
lst_sort = sorted(lst)


os.chdir('..')
with open('answer.txt', 'w') as answer:
    for line in lst_sort:
        answer.write(line + '\n')
