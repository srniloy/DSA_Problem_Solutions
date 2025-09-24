def solve():
    s = input()
    aCount = 0
    for c in s:
        if c == 'A':
            aCount += 1
        else:
            aCount -= 1

    print('A' if aCount > 0 else 'B')

t = int(input())
for _ in range(t):
  solve()
