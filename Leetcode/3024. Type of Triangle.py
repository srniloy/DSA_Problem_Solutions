class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        d = len(set(nums))
        if (nums[0] + nums[1]) > nums[2] and (nums[0] + nums[2]) > nums[1] and (nums[1] + nums[2]) > nums[0]:
            if d == 1:
                return "equilateral"
            elif d == 2:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"



print(Solution().triangleType([8, 4, 4]))