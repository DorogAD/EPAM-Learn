"""
https://stepik.org/lesson/24470/step/14?unit=6776


Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.

Sample Input:

this is a text
"this' !is. ?n1ce,

Sample Output:

htis si a etxt
"htis' !si. ?1nce,
"""

import re
import sys


def replace_letters(word):
    return word.group(2) + word.group(1) + word.group(3)


pattern = r'\b(\w)(\w)(\w*)\b'

for line in sys.stdin:
    line = line.rstrip()
    result = re.sub(pattern, replace_letters, line)
    print(result)
