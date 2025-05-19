def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 2:
        if a[0] == 0 and a[1] == 0:
            print("YES")
        elif a[0] == 1 and a[1] == 1:
            print("YES")
        else:
            print("NO")
    else:
        if all(x == 0 for x in a):
            print("YES")
        elif all(x == 1 for x in a):
            print("YES")
        else:
            az = any(a[i] == 0 and a[i + 1] == 0 for i in range(n - 1))
            if az:
                print("YES")
            else:
                print("NO")



t = int(input())
for _ in range(t):
    solve()