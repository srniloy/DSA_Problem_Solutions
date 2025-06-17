def solve():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    l = max(0, arr[-1] - s)
    r = max(0, s - arr[0])

    max_val = max(l, r)
    min_val = min(l, r)

    if max_val != 0 and min_val != 0:
        ans = max_val + (min_val * 2)
        print(ans)
    else:
        ans = max(min_val, max_val)
        print(ans)


t = int(input())
for _ in range(t):
    solve()
