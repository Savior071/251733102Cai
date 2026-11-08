L, M = map(int, input().split())
total = L + 1
s = set()
for i in range(M):
    l, r = map(int, input().split())
    for j in range(l, r + 1):
        s.add(j)
trees = total - len(s)
print(trees)