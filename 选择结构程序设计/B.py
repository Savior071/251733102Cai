def collatz(n):
    if n % 2 != 0:
        return 3 * n + 1
    else:
        return n//2
n = int(input())
print(collatz(n))