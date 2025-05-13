class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        l, r = 0,n-1
        while l <= r:
            s = numbers[l]+numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s > target:
                r -= 1
            else:
                l += 1



s = Solution()

print(s.twoSum([2,7,11,15], 9))