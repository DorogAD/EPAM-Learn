"""
https://stepik.org/lesson/3369/step/11?unit=952

Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого
верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):

Sample Input:

5

Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""

# size = int(input())
size = 7
matrix = []

for i in range(size):
    matrix.append([0] * size)

matrix[0][0] = 1

n = 1

while 0 in matrix[size // 2]:

    for i in range(n - 1, n):
        for j in range(size):
            if matrix[i][j] == 0:
                matrix[i][j] = matrix[i][j - 1] + 1

    for i in range(size):
        for j in range(size - n, size - n + 1):
            if matrix[i][j] == 0:
                matrix[i][j] = matrix[i - 1][j] + 1

    for i in range(size - n, size - n + 1):
        for j in range(size - 1, -1, -1):
            if matrix[i][j] == 0:
                matrix[i][j] = matrix[i][j + 1] + 1

    for i in range(size - 1, -1, -1):
        for j in range(n - 1, n):
            if matrix[i][j] == 0:
                matrix[i][j] = matrix[i + 1][j] + 1

    n += 1

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()
