n = int(input())

generalsH = list(map(int,input().split()))

maxH = max(generalsH)
maxI = generalsH.index(maxH)
minH = min(generalsH)
minI = generalsH.index(minH)

for i in range(n):
    if generalsH[i] > maxH:
        maxH = generalsH[i]
        maxI = i
    if generalsH[i] <= minH:
        minH = generalsH[i]
        minI = i

print(maxI + (n - minI - 1) - (1 if maxI > minI else 0))


