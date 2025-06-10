from bisect import bisect_right

def solve():
    n = int(input())
    prices = list(map(int, input().split()))
    q = int(input())
    m_values = [int(input()) for _ in range(q)]

    prices.sort()
    for m in m_values:
        print(bisect_right(prices, m))

solve()