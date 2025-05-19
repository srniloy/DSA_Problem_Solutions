def solve():
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    else:
        print(b)

t = int(input())
for _ in range(t):
    solve()