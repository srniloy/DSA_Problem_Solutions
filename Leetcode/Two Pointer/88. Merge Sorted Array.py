class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l, r= m-1, n-1
        last = m+n-1
        while l >= 0 and r >= 0:
            if nums1[l] > nums2[r]:
                nums1[last] = nums1[l]
                l -= 1
                last -= 1
            else:
                nums1[last] = nums2[r]
                r -= 1
                last -= 1


        while last >= 0 and r >= 0:
            nums1[last] = nums2[r]
            r -= 1
            last -= 1
        print(nums1)







s = Solution()
s.merge([1,2,4,5,6,0], 5, [3], 1)