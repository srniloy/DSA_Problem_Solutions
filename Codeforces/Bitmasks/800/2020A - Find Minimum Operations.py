def solve():
    n, k = map(int, input().split())
    if k == 1:
        print(n)
        return
    res = 0
    while n > 0:
        res += n % k
        n = int(n/k)
    print(res)




t = int(input())
for _ in range(t):
    solve()