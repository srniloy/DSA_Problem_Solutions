def solve():
    s = input().strip()
    num = int(s)
    found = False
    for split_pos in [1, 2, 3]:
        a_str = s[:split_pos]
        b_str = s[split_pos:]
        if len(a_str) > 1 and a_str[0] == '0':
            continue
        if len(b_str) > 1 and b_str[0] == '0':
            continue
        a = int(a_str)
        b = int(b_str)
        if (a + b) ** 2 == num:
            print(a, b)
            found = True
            break
    if not found:
        print(-1)


t = int(input())
for _ in range(t):
    solve()