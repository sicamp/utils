#usage: python3 to_enlisted.py source.csv dest.csv
#compile table for enlisted page

from sys import argv
import csv

take_column = 3
take_values = {'Y', 'NY'}
dest_columns = [0, 1, 19, 20, 21, 4]

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

source = readTable(argv[1])
table = [source[0]] + [row for row in source if row[take_column] in take_values]
table = list(zip(*table))
dest = [table[i] for i in dest_columns]
dest = list(zip(*dest))

writeTable(argv[2], dest)

