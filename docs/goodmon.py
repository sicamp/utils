f = open("vstupit.csv", "r")
s = f.read()
t = ''
bal = 0
for i in range(len(s)):
    if s[i] == '"':
        bal+=1
    elif s[i] != '\n' or bal % 2 == 0:
        t = t + s[i]

g = open("vstupit1.csv", "w")
g.write(t)
g.close()

