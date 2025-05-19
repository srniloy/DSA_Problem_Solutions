def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    sb = b.copy()
    sb.sort()
    res = {}
    l, r = n-1, m-1
    while l >= 0 and r >= 0:
        if a[l] <= sb[r]:
            res[sb[r]] = l+1
            r-=1
        else:
            l-=1

    for v in b:
        print(res.get(v,0), end=' ')




solve()