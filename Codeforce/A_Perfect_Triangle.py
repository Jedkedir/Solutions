cases = int(input())
while cases:
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    op = float('inf')
    for i in range(n-2):
        op = min(op,arr[i+2]-arr[i])
    print(op)
    cases -= 1