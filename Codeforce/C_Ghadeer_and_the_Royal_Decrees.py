cases = int(input())
while cases:
    size, op = map(int, input().split())
    arr = list(map(int, input().split()))
    current_max = max(arr)
    res = []
    for _ in range(op):
        o, l, r = input().split()
        l, r = int(l), int(r)
        if l <= current_max <= r:
            if o == '+':
                current_max += 1
            else:
                current_max -= 1
        res.append(str(current_max))
    print(*res)
    cases -= 1