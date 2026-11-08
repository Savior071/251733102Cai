L,R = map(int,input().split())
c = 0
for i in range(L,R + 1):
    s = str(i)
    c += s.count('2')
print(c)