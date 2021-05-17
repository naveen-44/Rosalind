s1 = str(input())
s2 = str(input())
c = 0
for i in range(len(s1)):
    x = s1[i]
    y = s2[i]
    if x!=y:
        c+=1
print(c)
