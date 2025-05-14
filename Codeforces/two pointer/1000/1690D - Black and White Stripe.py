def solve():
    n, k = map(int, input().split())
    bs = list(str(input()))

    l, r = 0, 0
    maxB = 0
    cb = 0
    while r < k:
        if bs[r] == 'B':
            cb += 1
        r+=1
        maxB = cb
    while r < n:
        if bs[r] == 'B':
            cb += 1
        if bs[l] == 'B':
            cb -= 1
        if cb > maxB:
            maxB = cb
        r+=1
        l+=1

    if maxB >= k:
        print(0)
    else:
        print(k-maxB)








t = int(input())
for _ in range(t):
    solve()