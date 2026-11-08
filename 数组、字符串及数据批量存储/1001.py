T = int(input())
for i in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    range_val = max(nums) - min(nums)
    avg = sum(nums) / n
    variance = sum((x - avg) ** 2 for x in nums) / n
    print(f"{range_val} {variance:.3f}")