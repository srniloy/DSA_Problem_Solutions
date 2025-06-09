def solve():
    n = int(input())
    vec = list(map(int, input().split()))
    total_xor = 0
    for num in vec:
        total_xor ^= num

    if total_xor == 0:
        print("YES")
        return

    current_xor = 0
    cnt = 0
    for num in vec:
        current_xor ^= num
        if current_xor == total_xor:
            cnt += 1
            current_xor = 0

    print("YES" if cnt >= 2 and current_xor == 0 else "NO")


t = int(input())
for _ in range(t):
    solve()