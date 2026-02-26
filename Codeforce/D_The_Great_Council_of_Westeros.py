cases = int(input())
while cases > 0:
    n, m = map(int, input().split())
    houses = []
    for i in range(n):
        arr = list(map(int, input().split()))
        arr.sort()
        houses.append([arr, i + 1])
    houses.sort(key=lambda x: x[0][0])
    p = []
    for h in houses:
        p.append(h[1])
    possible = True
    for i in range(n):
        for j in range(m):
            if houses[i][0][j] != i + (j * n):
                possible = False
                break
        if not possible:
            break
    if possible:
        print(*p)
    else:
        print("-1")
    cases -= 1