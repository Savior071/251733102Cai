results = []
for i in range(1,100):
    for j in range(i+1,2000):
        n = i * j
        m = str(i) + str(j) +str(n)
        if len(m) == 9 and set(m) == set('123456789'):
            results.append((n,i,j))
results.sort(key=lambda x:(x[0],x[1]))
for n,i,j in results:
    print(f'{n} = {i} x {j}')