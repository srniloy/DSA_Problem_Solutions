
def solve():
    n = int(input())
    figures = {
        "tetrahedron": 4,
        "cube": 6,
        "octahedron": 8,
        "dodecahedron": 12,
        "icosahedron": 20
    }
    res = 0
    for _ in range(n):
        res += figures.get(input().lower(), 0)
    print(res)


solve()