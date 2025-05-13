from math import ceil


# def Solve():
#     n, k = list(map(int, input().split()))
#     s = list(input())
#     if 'B' not in s:
#         print(0)
#         return
#     l, r = 0, n-1
#     res = 0
#     st, ed = -1, -1
#     # print(s)
#
#     while l <= r:
#         if 'B' == s[l] and st < 0:
#             st = l
#
#         if 'B' == s[r] and ed < 0:
#             ed = r
#         l+=1
#         r-=1
#
#     # print(st, ed)
#     print(ceil((ed - st+1)/k))
def Solve():
    n, k = list(map(int, input().split()))
    s = list(input())
    if 'B' not in s:
        print(0)
        return

    i=0
    res = 0
    while i < n:
        if 'B' == s[i]:
            res+=1
            i+=k
        else:
            i+=1

    print(res)



t = int(input())
for _ in range(t):
    Solve()