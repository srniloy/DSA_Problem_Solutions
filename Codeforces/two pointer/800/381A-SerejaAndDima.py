n = int(input())

nums = list(map(int, input().split()))

l, r = 0, len(nums)-1
sPoints, dPoints = 0, 0
turn = 0
while l <= r:
    maxV = 0
    if nums[l] > nums[r]:
        maxV = nums[l]
        l += 1
    else:
        maxV = nums[r]
        r -= 1

    if turn == 0:
        sPoints += maxV
        turn = 1
    else:
        dPoints += maxV
        turn = 0
print(f"{sPoints} {dPoints}")
