n = int(input())
a = list(map(int, input().split()))
a.sort()
ok = False
ans = []
for i in range(2, n):
    if a[i-2] + a[i-1] > a[i]:
        ans = [a[i-2], a[i-1], a[i]]
        ok = True
        break
if ok:
    print(ans[0], ans[1], ans[2])
else:
    print("No solution")
