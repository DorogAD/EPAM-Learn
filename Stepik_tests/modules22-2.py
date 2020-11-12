"""
Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями,
но он не смог понять какой из паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать,
какой из паролей служит ключом для расшифровки файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.

Примечание:
Для того, чтобы считать все данные из бинарного файла, можно использовать, например, следующий код:

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
"""
import simplecrypt
import urllib
from urllib import request

encrypted = urllib.request.urlopen('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').read()
# print(encrypted)
# with open("encrypted.bin", "rb") as f1:
#     enc = f1.read()
#     print(enc)

with open("passwords.txt", "rt") as f2:
    for psw in f2:
        try:
            print(psw)
            res = simplecrypt.decrypt(psw.strip(), encrypted)
            print(res.decode("utf-8"))
            break
        except simplecrypt.DecryptionException:
            pass
