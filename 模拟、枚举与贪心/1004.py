t = int(input())
s = []
for i in range(t):
    s.append(input())
d = {'zero':'0','two':'2','four':'4','six':'6','nine':'9'}
for i in s:
    st = ''
    for k,v in d.items():
        i = i.replace(k,v)
    for j in i:
        if j in '02469':
            st += j
    print(st)