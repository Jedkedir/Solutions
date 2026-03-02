t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    if total % n != 0:
        print("-1")
    else:
        average = total // n
        k = 0
        for candies in arr:
            if candies > average:
                k += 1
        print(k)
    t -= 1