def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max_count = 0
    for i in range(n):
        for j in range(i, n):
            if (a[i] + a[j]) % 2 == 0:
                current_count = j - i + 1
                if current_count > max_count:
                    max_count = current_count
    print(n - max_count)

t = int(input())
for _ in range(t):
    solve()