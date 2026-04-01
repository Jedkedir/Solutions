n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

printed,i = 0,0,0
while k:
    while i < n and arr[i] - printed <=0:
        i+=1
    if i < n:
        diff = arr[i] - printed
        print(diff)
        printed += diff
    else:
        print(0)
    k -= 1