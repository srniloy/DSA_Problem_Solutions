def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    mn = float('inf')
    mx = float('-inf')
    total_sum = 0

    for num in a:
        total_sum += num
        mn = min(mn, num)
        mx = max(mx, num)

    cnt = a.count(mx)

    if mx - mn > k + 1 or (mx - mn == k + 1 and cnt > 1):
        print("Jerry")
    else:
        print("Tom" if total_sum % 2 else "Jerry")


t = int(input())
for _ in range(t):
    solve()
