n = input()
a,b = map(int,n.split())
if a < b:
    print('<')
if a==b:
    print('=')
if a > b:
    print('>')