def solve():
    n = int(input())
    a = list(map(int, input().split()))
    res = -1
    for i in range(len(a)):
        xor = 0
        for j in range(len(a)):
            if a[i] == a[j]:
                continue
            xor ^= a[j]
        if xor == a[i]:
            res = a[i]
            break
    print(res if res >= 0 else a[n-1])



t = int(input())
for _ in range(t):
    solve()