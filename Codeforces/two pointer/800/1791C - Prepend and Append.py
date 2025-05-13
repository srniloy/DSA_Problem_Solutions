
def initialStringLen():
    n = int(input())
    s = list(input())
    l, r = 0, len(s)-1
    res = 0
    while l <= r:
        if s[l] == s[r]:
            res = (r-l)+1
            break
        l+=1
        r-=1
    print(res)


t = int(input())
for _ in range(t):
    initialStringLen()