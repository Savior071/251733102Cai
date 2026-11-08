n, t = map(int, input().split())
s = input().strip()
pos_dot = s.index('.')
arr = list(s)
i = pos_dot + 1
while t > 0 and i < len(arr):
    if int(arr[i]) >= 5:
        j = i - 1
        arr[j] = str(int(arr[j]) + 1)
        while j >= 1 and arr[j] == '10':
            arr[j] = '0'
            j -= 1
            arr[j] = str(int(arr[j]) + 1)
        arr = arr[:i]
        t -= 1
        i = j
    else:
        i += 1
res = ''.join(arr)
if '.' in res:
    integer_part, decimal_part = res.split('.')
    decimal_part = decimal_part.rstrip('0')
    if decimal_part == '':
        print(integer_part)
    else:
        print(integer_part + '.' + decimal_part)
else:
    print(res)