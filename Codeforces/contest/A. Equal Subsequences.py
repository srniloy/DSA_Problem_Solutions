def solve():
    n, k = map(int, input().split())
    ans = '1' * k + '0' * (n - k)
    print(ans)

t = int(input())
for _ in range(t):
    solve()
