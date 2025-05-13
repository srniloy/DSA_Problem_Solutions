
def favSequence():
    n = int(input())
    nums = list(map(int, input().split()))
    res = [0 for i in range(n)]
    l,r = 0, n-1
    for i in range(n):
        if i%2==0:
            res[i] = nums[l]
            l += 1
        else:
            res[i] = nums[r]
            r -= 1
    print(" ".join(str(v) for v in res))



t = int(input())
for _ in range(t):
    favSequence()