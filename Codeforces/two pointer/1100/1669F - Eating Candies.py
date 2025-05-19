import math
def solve():
    n = int(input())
    a = list(map(int, input().split()))

    l, r = 0, n-1
    aw, bw = a[l], a[r]
    maxc = 0
    c = 2
    while l < r:
        if aw == bw and c > maxc:
            maxc = c
        if aw < bw:
            l += 1
            aw += a[l]
        else:
            r -= 1
            bw += a[r]
        c += 1
    print(maxc)





t = int(input())
for _ in range(t):
    solve()