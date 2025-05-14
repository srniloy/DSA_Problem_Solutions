def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    l, r = 0, n-1
    score = 0
    a.sort()
    while l < r:
        s = a[l]+a[r]
        if s == k:
            score+=1
            l+=1
            r-=1
        elif s > k:
            r -= 1
        else:
            l += 1
    print(score)




t = int(input())

for _ in range(t):
    solve()