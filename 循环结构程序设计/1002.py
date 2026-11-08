n = int(input())
m = 0
for i in range(1,n+1):
    for j in range(i):
        m = m + 1
        print(f'{m:4d}',end='')
    print()