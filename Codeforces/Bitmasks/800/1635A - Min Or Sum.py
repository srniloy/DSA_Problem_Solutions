def solve():
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(n):
        res |= a[i]
    print(res)



t = int(input())
for _ in range(t):
    solve()