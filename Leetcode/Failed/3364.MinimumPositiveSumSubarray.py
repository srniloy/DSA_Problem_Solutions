import sys
class Solution(object):
    def minimumSumSubarray(self, nums, l, r):

        def kMinSubArray(nums, k):
            if k == 1:
                minV = max(nums)
                for i in range(0, len(nums)):
                    if minV > nums[i] > 0:
                        minV = nums[i]
                return minV

            current = 0
            for i in range(k):
                current += nums[i]

            minV = current

            for i in range(k, len(nums)):
                current -= nums[i-k]
                current += nums[i]
                if minV > current > 0 or minV < 0:
                    minV = current
            return minV

        minL = []
        i = l
        while i <= r:
            minL.append(kMinSubArray(nums, i))
            i+=1
        print(minL)
        minL = [v for v in minL if v > 0]
        res = min(minL) if len(minL)>0 else 0

        return -1 if res <= 0 else res

s = Solution()
print(s.minimumSumSubarray([21,-21,-10,-24,16,5,-21,18], 3, 6))