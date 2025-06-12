def solve():
    n = int(input())
    d = [100, 20, 10, 5, 1]
    res = 0
    for v in d:
        count = n//v
        res += count
        n -= count*v
    print(res)

solve()