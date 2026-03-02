t = int(input())

while t:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    possible = True
    for i in range(1, n):
        if arr[i] - arr[i-1] > 1:
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("NO")
    t -= 1

