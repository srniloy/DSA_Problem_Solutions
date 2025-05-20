class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r1 = 0
        for i in range(len(nums)):
            r1 ^= nums[i]
        diff_bit = 1 # 000001
        while not (diff_bit & r1):
            r1 = r1 << 1

        l2, l3 = 0, 0
        for v in nums:
            if diff_bit & v:
                l2 ^= v
            else:
                l3 ^= v
        return [l2, l3]

print(Solution().singleNumber([7,1,7,2,6,6,3,1]))
