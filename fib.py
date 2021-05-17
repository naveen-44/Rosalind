n,k = list(map(int,input().split()))
tt = 1
a = 0
b = 1
while tt<n:
#     print(a,b)
    t = b
    b+= (a*k)
    a+=t
    b-=t
    tt+=1
print(a+b)
