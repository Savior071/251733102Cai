import math
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
t = input().strip()
p_str = t + t[-2::-1]
p = int(p_str)
if is_prime(p):
    print("prime")
else:
    print("noprime")