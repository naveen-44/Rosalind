ttt = 9
m = 0
ans = ''
for _ in range(ttt):
    x = str(input())
    s = str(input())
    score = 0
    space = 0
    for ss in s:
        if ss == "C" or ss == "G":
            score += 1
        if ss == " ":
            space += 1
    score = round(score*100/(len(s)-space),5)
    print(score)
    if score>m:
        m = score
        ans = x[1:]
print(ans)
print(m)
