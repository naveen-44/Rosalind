ans = [0 for i in range(4)]
dna = ['A','C','G','T']
s = str(input())
for i in s:
    for j in range(len(dna)):
        x = dna[j]
        if x == i:
            ans[j]+=1
ss = ''
for i in ans:
    ss += str(i)
    ss += ' '
print(ss)
