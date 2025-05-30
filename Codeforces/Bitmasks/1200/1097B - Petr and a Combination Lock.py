def solve():
    n = int(input())
    angles = [int(input()) for _ in range(n)]
    found = False

    for mask in range(0, 1 << n):
        total = 0
        for i in range(n):
            if mask & (1 << i):
                total -= angles[i]
            else:
                total += angles[i]
        if total % 360 == 0:
            found = True
            break

    print("YES" if found else "NO")

solve()