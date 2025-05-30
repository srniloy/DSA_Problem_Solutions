class Solution(object):
    def minCuttingCost(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        def compute_cost(x):
            if x <= k:
                return 0
            cuts = (x - 1) // k
            cost = 0
            remaining = x
            for _ in range(cuts):
                piece = k
                remaining -= piece
                cost += piece * remaining
            return cost
        return compute_cost(n) + compute_cost(m)