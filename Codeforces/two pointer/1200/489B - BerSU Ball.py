import math
def solve():
    n = int(input())
    b = list(map(int, input().split()))

    m = int(input())
    g = list(map(int, input().split()))

    b.sort()
    g.sort()
    l, r = 0, 0
    count = 0
    while l < n and r < m:

        if b[l] == g[r] or abs(b[l]-g[r]) == 1:
            count+=1
            l+=1
            r+=1
        elif b[l] < g[r]:
            l+=1
        else:
            r+=1
    print(count)



solve()