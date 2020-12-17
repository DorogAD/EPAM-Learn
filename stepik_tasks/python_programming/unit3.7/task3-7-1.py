"""
https://stepik.org/lesson/3380/step/1?unit=963



Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на
стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""

num = int(input())

games_list = []
for i in range(num):
    one_game = input().split(';')
    games_list.append(one_game)

# games_list = [['Спартак', '9', 'Зенит', '10'], ['Локомотив', '12', 'Зенит', '3'], ['Спартак', '8', 'Локомотив', '15']]

result = {}
for i in games_list:
    if i[0] not in result.keys():
        if int(i[1]) > int(i[3]):
            result[i[0]] = 'w'
        elif int(i[1]) < int(i[3]):
            result[i[0]] = 'l'
        else:
            result[i[0]] = 'd'
    elif i[0] in result.keys():
        if int(i[1]) > int(i[3]):
            result[i[0]] += 'w'
        elif int(i[1]) < int(i[3]):
            result[i[0]] += 'l'
        else:
            result[i[0]] += 'd'
    if i[2] not in result.keys():
        if int(i[1]) > int(i[3]):
            result[i[2]] = 'l'
        elif int(i[1]) < int(i[3]):
            result[i[2]] = 'w'
        else:
            result[i[2]] = 'd'
    elif i[2] in result.keys():
        if int(i[1]) > int(i[3]):
            result[i[2]] += 'l'
        elif int(i[1]) < int(i[3]):
            result[i[2]] += 'w'
        else:
            result[i[2]] += 'd'

for key, value in result.items():
    games_count = len(value)
    wins_count = value.count('w')
    draws_count = value.count('d')
    print(key + ':' + str(games_count) + ' ' + str(wins_count) + ' ' + str(draws_count) + ' ' + str(
        games_count - wins_count - draws_count) + ' ' + str(wins_count * 3 + draws_count * 1))
