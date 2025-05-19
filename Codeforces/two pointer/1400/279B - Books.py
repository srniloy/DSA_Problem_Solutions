def solve():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    l, r = 0, 0
    s = 0
    count=0
    while r < n:
        s += a[r]
        if s <= t:
            count+=1
        else:
            s -= a[l]
            l+=1
        r+=1
    print(count)



solve()


# 6 10
# 2 3 4 2 1 1