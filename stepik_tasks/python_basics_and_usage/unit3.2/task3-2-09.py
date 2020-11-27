"""
https://stepik.org/lesson/24470/step/9?unit=6776

Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

Sample Input:

zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Sample Output:

zabcz
zzxzz
"""

import re
import sys

pattern = r'.*z.{3}z.*'

for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(pattern, line)
    for lines in result:
        print(lines)
