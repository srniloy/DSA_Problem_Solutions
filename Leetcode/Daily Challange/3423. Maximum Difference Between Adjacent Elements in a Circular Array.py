class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        nums.sort()
        fp=-1
        # if nums[0] < 0:
        #     for v in nums:
        #         if v >= 0:
        #             fp = v
        #             break
        #     if fp >= 0:
        #         return abs(fp - nums[0])
        if nums[0] < 0:
            return abs(nums[len(nums) - 1]) - nums[0]-1

        return nums[len(nums)-1] - nums[0]


print(Solution().maxAdjacentDistance([3,2,-5,-3]))