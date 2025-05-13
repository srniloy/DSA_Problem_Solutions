
n = int(input())
feelings = ""
for i in range(1, n+1):
    feelings += "I love" if i % 2 == 0 else "I hate"
    feelings += " it" if i == n else " that "
print(feelings)




