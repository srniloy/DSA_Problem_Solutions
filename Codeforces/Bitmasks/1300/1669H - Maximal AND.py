# https://codeforces.com/problemset/problem/1669/H
# Unsolved


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    bitCount = {}
    for i in range(30, -1, -1):
        for v in a:
            if ((v << i) & 1) == 1:
                bitCount[i] = bitCount.get(i, 0) + 1
    print(bitCount)
    


def test():
    a = (1 << 30) | 3
    b = (1 << 30) | 1
    print(a & b)

# t = int(input())
# for _ in range(t):
#     solve()

solve()