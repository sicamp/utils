#usage: python3 mail.py list.csv template.html

from sys import argv
from os import system
import csv
import time

def readTable(fname):
    lines = csv.reader(open(fname, newline=''))#, delimiter=',', quotechar='"')
    table = []
    for l in lines:
        table.append([s.strip() for s in l])
    
    return table

source = readTable(argv[1])
text = open(argv[2]).read()
cnt = 0
for row in source:
    print(row)
    print(row[22])
    open("mail.html", "w").write(text.replace("$NAME", row[1]).replace("$SURNAME", row[0]).replace("$PAR", row[3]))
#    system('mail -a"From:ЛКЛ <mail@sicamp.ru>" -s "Вы зачислены в ЛКЛ 2016!" ' + row[3] + ' < mail.html')
    print(system('mail -a"Content-Type: text/html; charset=UTF-8" -a"From:=?utf-8?B?ЛКЛ?= <mail@sicamp.ru>" -s "=?utf-8?B?ЛКЛ 2016 - Анкета зачисленного?=" ' + row[22] + ' < mail.html'))
    cnt += 1
    if cnt % 5 == 0:
        time.sleep(10)
    else:
        time.sleep(1)

