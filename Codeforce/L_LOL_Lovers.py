n = int(input())
s = input().strip()

totalL = s.count('L')
totalO = n - totalL

prefixL = 0
prefixO = 0

for i in range(n - 1):  # k = i+1
    if s[i] == 'L':
        prefixL += 1
    else:
        prefixO += 1
    
    # Check conditions
    if prefixL != totalL - prefixL and prefixO != totalO - prefixO:
        print(i + 1)
        break
else:
    print(-1)