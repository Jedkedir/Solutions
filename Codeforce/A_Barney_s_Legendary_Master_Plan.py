t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    unique = set(arr)
    k = len(unique)
    if k == 0:
        print("0")
    else:
        print(2 * k - 1)
    t -= 1