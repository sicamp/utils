
def readTable(fname):
    f = open(fname, "r")
    lines = f.readlines()
    table = []
    for l in lines:
        table.append([s.strip() for s in l.strip().split(',') if len(s.strip()) > 0])
    
    return table

def writeTable(fname, table):
    f = open(fname, "w")
    lines = [','.join(row) for row in table]
    f.write('\n'.join(lines))
    f.close()

table = readTable("vstupit1.csv")
for row in table:
    for i in range(1, len(row)):
        row[i] = '1' if int(row[i]) > 0 else '0'

writeTable("vstupit2.csv", table)
