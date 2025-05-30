import math

class Solution(object):
    def sumOfLargestPrimes(self, s):
        """
        :type s: str
        :rtype: int
        """
        primes = set()

        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            max_divisor = math.isqrt(n) + 1
            for d in range(3, max_divisor, 2):
                if n % d == 0:
                    return False
            return True

        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                num_str = substring.lstrip('0')
                if not num_str:
                    continue
                num = int(num_str)
                if is_prime(num):
                    primes.add(num)

        sorted_primes = sorted(primes, reverse=True)
        return sum(sorted_primes[:3]) if len(sorted_primes) >= 3 else sum(sorted_primes)


s = Solution()
print(s.sumOfLargestPrimes("111"))