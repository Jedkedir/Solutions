cases = int(input())
while cases:
    n = int(input())
    a = list(map(int,input().split()))
    target = int(input())
    if n == 1 :
        print("YES" if a[0]== target else "NO")
    else:
        if min(a) <= target <= max(a):
            print("YES")
        else:
            print("NO")
    cases -= 1