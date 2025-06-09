def solve():
    a, b = map(int, input().split())

    if a == b:
        print(0)
    else:
        diff = abs(a - b)
        answer = 0

        for i in range(10, 0, -1):
            answer += diff // i
            diff %= i

        print(answer)


t = int(input())
for _ in range(t):
    solve()