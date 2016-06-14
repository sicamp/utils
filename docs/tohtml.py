
from sys import argv
def readTable(fname):
    f = open(fname, "r")
    lines = f.readlines()
    table = []
    for l in lines:
        if l == '\n':
            table.append(['123'])
        else:
            table.append([s.strip() for s in l.strip().split(',') if len(s.strip()) > 0])
    
    return table

def writeHtml(fname, table):

    f = open(fname, "w")
    for row in table:
        line = '<tr>\n' + ''.join('<td>' + cell + '</td>' for cell in row) + '\n</tr>\n'
        f.write(line);
    f.close()

table = readTable(argv[1])
writeHtml(argv[2], table)

