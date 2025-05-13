def solve():
    n, m, p, q = map(int, input().split())
    possible = False
    if p == n:
        if m == q:
            possible = True
    else:
        k = n // p
        rem = n % p
        if rem == 0:
            if m == k * q:
                possible = True
        else:
            possible = True
    print("YES" if possible else "NO")

t = int(input())
for _ in range(t):
    solve()