'''
https://stepik.org/lesson/24469/step/7?unit=6775

Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.
'''
s = 'abababa'
t = 'aba'

start = 0
end = start + len(t)
end_len = len(s) + 1 - len(t)
counter = 0
print(start, end, end_len)
if t not in s:
    print(0)
elif s == t:
    print(1)
else:
    while start != end_len:
        word = s[start:end]
        if word == t:
            counter = counter + 1
        start = start + 1
        end = end + 1
            
    print(counter)
        

