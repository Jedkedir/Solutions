from collections import Counter
cases = int(input())
while cases:
    n = int(input())
    arr = list(map(int,input().split()))
    count = {}
    for x in arr:
        count[x] = count.get(x,0)+1
    majority = False
    for num in count:
        if count[num] > n//2:
            majority = True
            break
    if majority:
        print("YES")
    else :
        print("NO")
    cases -= 1