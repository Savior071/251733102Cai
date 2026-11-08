line = input()
a = line.split()
n = int(a[0])
x = int(a[1])
count = 0
for i in range(1,n+1):
    y = i
    while y>0:
        if y % 10 == x:
            count += 1
        y = y//10
print(count)