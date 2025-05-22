def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    for i in range(n):
        x ^= a[i]
    s = 0
    for i in range(n):
        s ^= (a[i]^x)
    print(x if s == 0 else -1)
t = int(input())
for _ in range(t):
    solve()
