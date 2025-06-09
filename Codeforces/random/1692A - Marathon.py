def solve():
    a = list(map(int, input().split()))
    res = 0
    for i in range(1, len(a)):
        if a[0] < a[i]:
            res += 1

    print(res)


t = int(input())
for _ in range(t):
    solve()