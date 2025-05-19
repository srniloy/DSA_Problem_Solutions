class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = []
        while n > 0:
            binary.append(n%2)
            n = int(n/2)
        binary.reverse()
        print(binary)
        return len(binary)

s = Solution()
print(s.hammingWeight(2))