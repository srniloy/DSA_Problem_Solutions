def solve():

    n = int(input())
    a = list(map(int, input().split()))
    even = 0
    lastodd = 0
    lasteven = 0

    for i in range(1, n + 1):
        if a[i-1] % 2 == 0:
            even += 1
            lasteven = i
        else:
            even -= 1
            lastodd = i

    print(lastodd if even > 0 else lasteven)

solve()