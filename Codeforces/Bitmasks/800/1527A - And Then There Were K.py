def solve():
    n = int(input())
    for i in range(31, -1, -1):
        if (1 << i) & n:
            print((1 << i)-1)
            break


t = int(input())
for _ in range(t):
    solve()