import math

def gcd_list(arr):
    g = 0
    for num in arr:
        g = math.gcd(g, num)
    return g

def solve_case(n, a):
    u = sorted(set(a))
    for v in u:
        B = []
        C = []
        for num in a:
            if num == v:
                B.append(num)
            else:
                C.append(num)
        if B and C:
            g = gcd_list(C)
            if g != v:
                print("Yes")
                res = []
                for num in a:
                    if num == v:
                        res.append(1)
                    else:
                        res.append(2)
                print(" ".join(map(str, res)))
                return
    print("No")

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    solve_case(n, a)
