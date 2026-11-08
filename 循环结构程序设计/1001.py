n = int(input())
m = -1
s = (2 * n) - 1
for i in range(1,n+1):
    m = m + 2
    print(' ' * (n - i) + "*" * m)
for i in range(2,n+1):
    s = s - 2
    print(' ' * (i - 1) + "*" * s)