"""
https://stepik.org/lesson/24470/step/10?unit=6776


Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\".

Sample Input:

\w denotes word character
No slashes here

Sample Output:

\w denotes word character
"""
import re
import sys

pattern = r'.*\\.*'

for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(pattern, line)
    for each_line in result:
        print(each_line)
