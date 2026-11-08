line = input()
a = line.split()
n = int(a[0])
k = int(a[1])
m = int(a[2])
p = list(range(n))
j = k
while len(p)>1:
    j = (j + m - 1) % len(p)
    p.pop(j)
print(p[0])