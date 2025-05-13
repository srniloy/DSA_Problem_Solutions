def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = a.copy()
    c.sort()
    res = "YES"
    for i in range(n):
        if a[i] % 2 != c[i] % 2:
            res = "NO"
            break
    print(res)

t = int(input())
for _ in range(t):
    solve()