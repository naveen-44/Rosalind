s = str(input())
t = str(input())
c = []
for i in range(len(s)-len(t)):
    g = s[i:i+len(t)]
    if g == t:
        c.append(i+1)
for i in c:
    print(i,end = " ")
