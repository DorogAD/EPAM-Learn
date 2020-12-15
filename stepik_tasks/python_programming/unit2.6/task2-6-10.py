"""
https://stepik.org/lesson/3369/step/10?unit=952

Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся
строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой
матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
"""

matrix = []
while True:
    short = input().split()
    if short[0] == 'end':
        break
    else:
        matrix.append(list(map(int, short)))

result = []

for i in range(len(matrix)):
    element = []
    for j in range(len(matrix[i])):
        if i == len(matrix) - 1 and j == len(matrix[i]) - 1:
            element.append(matrix[i - 1][j] + matrix[i - len(matrix) + 1][j] + matrix[i][j - 1] + matrix[i][
                j - len(matrix[i]) + 1])
        elif i == len(matrix) - 1:
            element.append(matrix[i - 1][j] + matrix[i - len(matrix) + 1][j] + matrix[i][j - 1] + matrix[i][j + 1])
        elif j == len(matrix[i]) - 1:
            element.append(matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j - len(matrix[i]) + 1])
        else:
            element.append(matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1])
    result.append(element)


for m in result:
    for k in m:
        print(k, end=' ')
    print()
