x = input().split(' ')
l,pos = int(x[0]) + 1,int(x[1]) - 1
odd = list(range(1,l,2))
even = list(range(2,l,2))
mid = (l // 2) if l%2==0 else (l//2)+1
if pos > mid:
    print(even[pos-mid])
else:
    print(odd[pos])
