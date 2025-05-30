def solve():
    n = int(input())
    bits = 0
    for i in range(32):
        bit = (n >> i) & 1
        if bit == 1:
            bits += 1
    print(bits)

solve()