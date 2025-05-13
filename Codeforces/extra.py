import sys


input = sys.stdin.readline

tt = int(input())
for _ in range(tt):
    n, k = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    brr = [0] + list(map(int, input().split()))

    vis1 = {}
    vis2 = {}
    ans = 0

    for i in range(1, n + 1):
        if arr[i] >= brr[i]:
            vis1[i] = 1
            ans += arr[i]
        else:
            vis2[i] = 1
            ans += brr[i]

    v = []
    for i in range(1, n + 1):
        if vis1.get(i, 0) == 0:
            v.append(arr[i])
        else:
            v.append(brr[i])

    v.sort(reverse=True)

    for i in range(min(k - 1, len(v))):
        ans += v[i]

    ans += 1
    print(ans)

