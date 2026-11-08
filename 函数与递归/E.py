T = int(input())
for i in range(T):
    line = input().strip()
    while not line:
        line = input().strip()
    parts = line.split()
    if len(parts) == 2:
        s, c = parts[0], parts[1]
    else:
        s = parts[0]
        c = input().strip()
    a = int(s)
    b = int(c)
    print(a * b)