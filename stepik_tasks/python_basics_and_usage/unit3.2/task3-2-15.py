"""
https://stepik.org/lesson/24470/step/15?unit=6776


Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.

Sample Input:

attraction
buzzzz

Sample Output:

atraction
buz
"""

import re
import sys


pattern = r'(\w)\1+'


for line in sys.stdin:
    line = line.rstrip()
    result = re.sub(pattern, r'\1', line)
    print(result)
