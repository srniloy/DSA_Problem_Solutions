import math

def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    max_limit = int(1e6) + 1
    is_prime = [True] * max_limit
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(max_limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, max_limit, i):
                is_prime[j] = False

    t_primes = set(i * i for i in range(2, max_limit) if is_prime[i])

    for x in nums:
        print("YES" if x in t_primes else "NO")



solve()
