def solve():
    x = int(input())
    res = 0
    pos = 0
    for i in range(32):
        bit = (x >> i) & 1
        if bit == 1:
            res = (1 << i)
            pos = i
            break
    if res == x:
        for i in range(32):
            bit = (x >> i) & 1
            if pos == i:
                continue
            if bit == 0:
                res = res | (1 << i)
                break

    print(res)


t = int(input())
for _ in range(t):
    solve()