cases = int(input())

while cases:
    x = list(map(int, input().split(' ')))
    if x[0] + x[1] == x[2] or x[1] + x[2] == x[0] or x[2] + x[0] == x[1]:
        print('YES')
    else:
        print('NO')
    cases -= 1
