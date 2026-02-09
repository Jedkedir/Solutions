cases = int(input())
while cases:
    n,m,p,q = list(map(int,input().split()))
    k = n//p
    r = n % p
    if r == 0:
        if m == k * q:
            print('YES')
        else:
            print("NO")
    else:
        print('YES')
    cases -= 1