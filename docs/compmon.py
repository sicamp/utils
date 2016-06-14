from sys import argv

def readTable(fname):
    f = open(fname, "r")
    lines = f.readlines()
    table = []
    for l in lines:
        if l == '\n':
            table.append(['123'])
        else:
            table.append([s.strip() for s in l.strip().split(',')])
    
    return table

def writeTable(fname, table):
    f = open(fname, "w")
    lines = [','.join(row) for row in table]
    f.write('\n'.join(lines))
    f.close()

def getrow(row):
    res = [0] * 5;
    bonus = int(row[-1])
    for i in range(5):
        for j in range(2):
            if ((bonus == 1 and i < 3) or bonus == 2) or row[pars[i] + j] == '1':
                res[i]+=1
        for j in range(2, parl[i]):
            if row[pars[i] + j] == '1':
                res[i] += 1
    return list(map(str, res))

t = readTable(argv[1])
d = [row[:2] for row in t]
parl = [3, 4, 4, 4, 4]
pars = [2, 3, 5, 7, 9]
for i in range(len(d)):
    d[i].extend(getrow(t[i]))
writeTable(argv[2], d)

