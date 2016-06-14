#usage: python3 order.py order.csv source.csv dest.csv
#rearrange rows in source.csv according to order.csv

from sys import argv
import csv

def readTable(fname):
    lines = csv.reader(open(fname, newline=''))#, delimiter=',', quotechar='"')
    table = []
    for l in lines:
        table.append([s.strip() for s in l])
    
    return table

def writeTable(fname, table):
    f = csv.writer(open(fname, "w", newline=''))
    for row in table:
        f.writerow(row)
def yo(s):
    return s.replace("ё", "е")

order = readTable(argv[1])
source = readTable(argv[2])
dest = [[order[i][j] for j in range(len(order[i]))] for i in range(len(order))]
numcols = len(order[0])
empty = [''] * numcols
used = set()
for row in source:
    for place in range(len(order)):
        if place in used:
            continue
        flag = True
        for i in range(numcols):
            curs = order[place][i] if i < len(order[place]) else ''
            if yo(curs.lower()) != yo(row[i].lower()):
                flag = False
                break
        if flag:
            used.add(place)
            dest[place].extend(row)
            break
    else:
        dest.append(empty + row)

#for row in dest:
#    if len(row) <= numcols:
#        row.extend(row)
#        row.extend('0')

writeTable(argv[3], dest)

