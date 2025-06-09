def solve():
    x = int(input())
    a = [0, 0, 0]
    actions = 0

    while any(v < x for v in a):
        a.sort()
        # We can increase the smallest one safely to match the second largest
        # or bring one closer to x while keeping the rule
        # always try to bring one up to x directly if valid
        for i in range(3):
            for inc in [x - a[i]]:
                if inc <= 0:
                    continue
                b = a[:]
                b[i] += inc
                ok = True
                for p in range(3):
                    for q in range(3):
                        if b[p] < (b[q] // 2):
                            ok = False
                if ok:
                    a = b
                    actions += 1
                    break
            else:
                continue
            break
    print(actions)

t = int(input())
for _ in range(t):
    solve()
