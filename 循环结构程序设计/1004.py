T = int(input())
for k in range(T):
    n = int(input())
    a = n // 2 + 1
    m = -1
    s = (2 * a) - 1
    for i in range(1,a+1):
        m = m + 2
        print(' ' * (a - i) + "*" * m)
    for i in range(2,a+1):
        s = s - 2
        print(' ' * (i - 1) + "*" * s)