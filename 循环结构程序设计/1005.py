import sys
for line in sys.stdin:
    n = int(line)
    m = n + 1
    for i in range(1,m+1):
        s = (m * 2) - (2 * i)
        print(' ' * (s) + "*" * i)
    for i in range(m - 1,0,-1):
        s = (m * 2) - (2 * i)
        print(' ' * (s) + "*" * i)