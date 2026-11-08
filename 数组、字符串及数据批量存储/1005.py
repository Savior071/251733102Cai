n = int(input())
num = list(map(int,input().split()))
if len(num) == 1:
    if num[0] == 15:
        print('DOWN')
    elif num[0] == 0:
        print("UP")
    else:
        print("-1")
else:
    if num[-1] > num[-2]:
        if num[-1] != 15:
            print('UP')
        else:
            print('DOWN')
    else:
        if num[-1] != 0:
            print('DOWN')
        else:
            print('UP')