def solve():
    n, m = map(int, input().split())

    a = list(str(input()))
    b = list(str(input()))

    l, r = 0, 0
    count = 0
    while l < n and r < m:
        if a[l] == b[r]:
            count += 1
            l += 1
        r += 1
    print(count)






t = int(input())
for _ in range(t):
    solve()