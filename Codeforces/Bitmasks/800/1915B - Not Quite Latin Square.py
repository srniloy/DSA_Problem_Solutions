def solve():
    mtx = [list(input()), list(input()), list(input())]

    for i in range(3):
        if '?' in mtx[i]:
            if 'A' not in mtx[i]:
                print("A")
            elif 'B' not in mtx[i]:
                print("B")
            else:
                print("C")
            break

t = int(input())
for _ in range(t):
    solve()