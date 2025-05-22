def solve():
    n = int(input())
    b = []
    for _ in range(n):
        m, s = input().split()
        b.append((int(m),int(s, 2)))
    b.sort()
    s1, s2 = 0, 0
    m = 0
    for v in b:
        if v[1] == 3:
            if s1 + s2 == 3:
                print(v[0] if v[0] < m else m)
            else:
                print(v[0])
            return
        elif v[1] == 1 or v[1] == 2:
            if s1 + s2 == 3:
                continue
            if s1 == 0:
                s1 = v[1]
                m+=v[0]
            elif s1 != v[1] and v[1] != 0:
                s2 = v[1]
                m+=v[0]
    print(-1 if s1 + s2 != 3 else m)








t = int(input())
for _ in range(t):
    solve()