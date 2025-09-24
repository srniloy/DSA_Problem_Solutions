from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            minIndex = i
            for j in range(i, len(nums)):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
        return nums


s = Solution()
s.sortArray([5,2,3,1])

#[5,2,3,1]