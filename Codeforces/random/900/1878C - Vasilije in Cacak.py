


def solve():
  n, k, x = map(int, input().split())
  min_sum = k * (k + 1) // 2
  max_sum = k * (2 * n - k + 1) // 2
  print("YES" if min_sum <= x <= max_sum else "NO")

t = int(input())
for _ in range(t):
  solve()