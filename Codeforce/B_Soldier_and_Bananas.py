x = input().split(' ')
k,n,w = int(x[0]),int(x[1]),int(x[2])
cost = 0
for i in range(1,w+1):
    cost += (i*k)
borrow = cost - n
print(borrow if borrow > 0 else 0)