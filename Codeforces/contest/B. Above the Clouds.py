def solve():
    length = int(input())
    text = input()

    is_present = False

    for mid in range(1, length - 1):
        left = text[:mid]
        center = text[mid]
        right = text[mid + 1:]

        if center in (left + right):
            is_present = True
            break

    print("Yes" if is_present else "No")


t = int(input())
for _ in range(t):
    solve()
