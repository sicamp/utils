#usage: python3 precomp.py source.csv dest.csv
#takes list of succesful submissions. makes table suitable to compmon.py

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

source = readTable(argv[1])
ts = set()
ls = set()
for r in source:
    ls.add(r[0])
    ts.add(r[1])
tl = list(reversed(sorted(list(ts))))
ll = list(sorted(list(ls)))
td = {}
ld = {}
for i in range(len(tl)):
    td[tl[i]] = i
for i in range(len(ll)):
    ld[ll[i]] = i
res = [[ll[i]] + [0] * len(tl) for i in range(len(ll))]
for row in source:
    res[ld[row[0]]][1 + td[row[1]]] = 1



#for row in dest:
#    if len(row) <= numcols:
#        row.extend(row)
#        row.extend('0')

writeTable(argv[2], res)

