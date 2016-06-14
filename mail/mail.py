#usage: python3 mail.py list.csv template.html

from sys import argv
from os import system
import csv
import time
import tempfile
import base64

import settings

# Заменяет в тексте письма плейсхолдеры на значения соотв. полей в строке
def personalize(text, user):
    for name in settings.placeholders:
        text = text.replace("$" + name, user[settings.placeholders[name]])

    return text

# Извлекает почтовый адрес из пользователя
def getEmail(user):
    return user[settings.email_field]

def encodeUTF(s):
    return base64.b64encode(s.encode("utf8")).decode("ascii")
# Отправляет пользователю письмо
def sendEmail(user):
    email = getEmail(user)
    print(user)
    print(email)

    mail_file = tempfile.NamedTemporaryFile(suffix='.html')
    mail_file.write(bytes(personalize(text, user), 'UTF-8'))
    mail_file.seek(0)
    print('Write to file ' + mail_file.name)
    print(system(
        "mail"
        " -a \"Content-Type: text/html; charset=UTF-8\""
        " -a \"From:=?utf-8?B?" + encodeUTF(settings.from_name) + "?= <" + settings.from_address + ">\""
        " -s \"=?utf-8?B?" + encodeUTF(settings.subject) + "?=\" " + email + " "
        " < " + mail_file.name
    ))

def readTable(fname):
    lines = csv.reader(open(fname, newline=''))
    table = []
    for l in lines:
        table.append([s.strip() for s in l])

    return table

source = readTable(argv[1])
text = open(argv[2]).read()
cnt = 0
for row in source:
    sendEmail(row)
    cnt += 1
    if cnt % 5 == 0:
        time.sleep(10)
    else:
        time.sleep(1)
