import sys

NEG_INF = -10**18

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    a = list(map(int, sys.stdin.readline().split()))

    curr = 0
    M_known = -float('inf')
    for i in range(n):
        if s[i] == '1':
            curr = max(curr + a[i], a[i])
            M_known = max(M_known, curr)
            if curr < 0:
                curr = 0
        else:
            curr = 0

    if M_known > k:
        print("No")
        continue

    zero_pos = -1
    for i in range(n):
        if s[i] == '0':
            zero_pos = i
            break

    if zero_pos == -1:
        if M_known == k:
            print("Yes")
            print(' '.join(map(str, a)))
        else:
            print("No")
        continue

    j = zero_pos
    suffix_sum = 0
    Lmax = -float('inf')
    foundL = False
    for i in range(j - 1, -1, -1):
        if s[i] != '1':
            break
        suffix_sum += a[i]
        Lmax = max(Lmax, suffix_sum)
        foundL = True
    L = Lmax if foundL else 0

    prefix_sum = 0
    Rmax = -float('inf')
    foundR = False
    for i in range(j + 1, n):
        if s[i] != '1':
            break
        prefix_sum += a[i]
        Rmax = max(Rmax, prefix_sum)
        foundR = True
    R = Rmax if foundR else 0

    if L >= 0 and R >= 0:
        x = k - L - R
    elif L >= 0 and R <= 0:
        x = k - L
    elif L <= 0 and R >= 0:
        x = k - R
    else:
        x = k

    print("Yes")
    for i in range(n):
        if s[i] == '0':
            if i == j:
                print(x, end=' ')
            else:
                print(NEG_INF, end=' ')
        else:
            print(a[i], end=' ')
    print()

