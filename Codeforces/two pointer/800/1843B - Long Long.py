def solve():
    n = int(input())
    a = list(map(int, input().split()))

    tn, tp = 0, 0
    for i in range(n):
        if a[i] < 0:
            tn += 1
        elif a[i] > 0:
            tp += 1
    count=0
    # if tn > tp:
    #     count += 1
    #     a = [(v * -1) for v in a]
    i = 0
    while i < n:
        if a[i] < 0:
            while i < n and a[i] <= 0:
                a[i] *= -1
                i += 1
            count+=1
        else:
            i+=1
    sum = 0
    for v in a:
        sum+=v
    print(sum, count)




t = int(input())
for _ in range(t):
    solve()