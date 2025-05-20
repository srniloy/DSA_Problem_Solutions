class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xFFFFFFFF
        while b != 0:
            temp = (a&b) << 1
            a = (a ^ b) & MASK
            b = temp & MASK
        return a if a <= 0x7FFFFFFF else ~(a ^ MASK)

