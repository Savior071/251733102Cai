ch=input()
n=ord(ch)-ord('A')+1
for i in range(1,n+1):
    print(" "*(n-i),end='')
    s = ''
    for j in range(i):
        s = s +chr(ord("A")+j)
    for k in range(i-2,-1,-1):
        s = s +chr(ord("A")+k)
    print(s)