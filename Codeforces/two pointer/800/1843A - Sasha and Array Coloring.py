
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) <= 1:
        print(0)
        return

    a.sort(reverse=True)
    cost = 0
    l, r = 0, n-1
    while l <= r:
        cost += a[l]-a[r]
        l+=1
        r-=1
    print(cost)




t = int(input())
for _ in range(t):
    solve()