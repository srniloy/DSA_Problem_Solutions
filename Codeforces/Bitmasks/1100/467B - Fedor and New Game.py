def solve():
    n, m, k = map(int, input().split())
    p = []
    for _ in range(m+1):
        p.append(int(input()))
    res = 0
    for i in range(m):
        match = p[m] ^ p[i]
        count = 0
        for j in range(32):
            bit = (match >> j) & 1
            if bit == 1:
                count+=1
        if count <= k:
            res += 1
    print(res)

solve()