import calendar
while True:
    try:
        y, m, x = map(int, input().split())
        target = str(x)
        c = 0
        _, days = calendar.monthrange(y, m)
        for d in range(1, days + 1):
            s = f"{y:04d}-{m:02d}-{d:02d}"
            c += s.count(target)
        print(c)
    except EOFError:
        break