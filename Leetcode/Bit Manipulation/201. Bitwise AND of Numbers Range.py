class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            bit = (left >> i) & 1
            if not bit:
                continue

            r = left % (1 << (i+1))
            d = (1 << (i+1)) - r
            if left - right < d:
                res = res | (1 << i)
        return res
