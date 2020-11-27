"""
https://stepik.org/lesson/24470/step/11?unit=6776


Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

Sample Input:

blabla is a tandem repetition
123123 is good too
go go
aaa

Sample Output:

blabla is a tandem repetition
123123 is good too
"""
import re
import sys

pattern = r'\b(\w+)\1\b'

for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(pattern, line)
    if len(result) > 0:
        print(line)
