"""
https://stepik.org/lesson/3380/step/3?unit=963



Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество d известных нам слов, после чего на d строках
указываются эти слова. Затем передаётся количество l строк текста для проверки, после чего l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:

stepic
champignons
the
"""

# count_words = int(input())
# test_words = [input().lower() for i in range(count_words)]

# count_strings = int(input())
# check_strings = [input() for i in range(count_strings)]

test_words = ['champions', 'we', 'are', 'stepik']
check_strings = ['We are the champignons', 'We Are The Champions', 'Stepic']

errors = []
for i in check_strings:
    for j in i.split():
        if j.lower() not in test_words:
            errors.append(j.lower())

errors = list(set(errors))

for i in errors:
    print(i)
