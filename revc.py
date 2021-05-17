s1 = ['A','T','C','G']
s2 = ['T','A','G','C']
s = str(input())
ans = []
for ss in s:
    ans.append(ss)
for i in range(len(ans)):
    for j in range(len(s1)):
        if ans[i]==s1[j]:
            ans[i]=s2[j]
            break
res = ''
for i in range(len(ans)):
    res+=str(ans[i])
print(res[::-1])
