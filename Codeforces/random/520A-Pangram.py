n = int(input())
letters = input()

letters = letters.lower()
letters = ''.join(sorted(letters))
count = 1
for i in range(0, n-1):
    if letters[i] != letters[i+1]:
        count += 1

print("YES" if count == 26 else "NO")