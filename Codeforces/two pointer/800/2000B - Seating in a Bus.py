def solve():
    n = int(input())
    a = list(map(int, input().split()))

    seat = {a[0]: 1}
    res = "YES"
    for i in range(1, n):
        seat[a[i]] = 1
        if seat.get(a[i]-1, 0) == 0 and seat.get(a[i]+1, 0) == 0:
            res = "NO"
            break

    print(res)




t = int(input())
for _ in range(t):
    solve()