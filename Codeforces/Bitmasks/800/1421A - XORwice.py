def solve():
    a, b = map(int, input().split())
    x = a & b
    print((a ^ x) + (b ^ x))


t = int(input())
for _ in range(t):
    solve()