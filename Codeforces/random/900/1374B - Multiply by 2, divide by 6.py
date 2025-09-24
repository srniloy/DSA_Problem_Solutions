

def solve():
    n = int(input())
    
    count2, count3 = 0, 0
    
    while not n%2:
        n//=2
        count2+=1
    
    while not n%3:
        n//=3
        count3+=1
    
    if n!=1 or count2 > count3:
        print(-1)
    else:
        print((count3-count2) + count3)

t = int(input())
for _ in range(t):
    solve()
