def solve():
    s = input()
    a = s[1:len(s)-1].split(',')
    if len(a) == 1 and a[0]=='':
        print(0)
        return
    a = [v.replace(' ', '') for v in a]
    print(len(list(dict.fromkeys(a))))



solve()