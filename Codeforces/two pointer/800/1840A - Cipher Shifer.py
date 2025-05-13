
def solve():
    n = int(input())
    s = list(input())
    l,r = 0, 1
    res = ""
    while r < n:
        if s[l] == s[r]:
            res += s[l]
            l = r+1
            r = l+1
        else:
            r += 1
    print(res)





t = int(input())
for _ in range(t):
    solve()