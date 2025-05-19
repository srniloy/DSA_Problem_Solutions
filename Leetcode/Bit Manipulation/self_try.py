def solve():
    n = 8
    a = n

    bits = []
    while n > 0:
        bits.append(n % 2)
        n = int(n/2)
    bits.reverse()
    print(''.join(str(b) for b in bits))
    print(bin(a))
    print('lsb: ', a & 1)

solve()