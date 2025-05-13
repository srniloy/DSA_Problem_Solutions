import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, x = map(int, sys.stdin.readline().split())
    if n == 1:
        if x == 0:
            print(-1)
        else:
            print(x)
    elif n == 2:
        if x == 0:
            print(2)
        else:
            a = 1
            b = x ^ a
            if b == 0:
                a = 2
                b = x ^ a
            print(a + b)
    else:
        if x == 0:
            if n % 2 == 0:
                print(n)
            else:
                print(n + 1)
        else:
            if n % 2 == 1:
                sum_ = (n - 1) + (x ^ (n - 1))
                print(sum_)
            else:
                sum_ = (n - 2) + 1 + (x ^ 1 ^ (n - 2))
                print(sum_)