x,y = map(int,input().split())
c = 0
start = min(x,y)
end = max(x,y)
for i in range(start, end+1):
    a = []
    s = str(i)
    for ch in s:
        a.append(int(ch))
    total = sum(a)
    if total % 5 == 0:
        c += 1
print(c)