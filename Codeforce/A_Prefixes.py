n = int(input())
s = list(input().strip())

operations = 0

for i in range(0, n, 2):
    if s[i] == s[i+1]:
        if s[i] == 'a':
            s[i] = 'a' 
            s[i+1] = 'b'
        else:  
            s[i] = 'b'
            s[i+1] = 'a'
        operations += 1

print(operations)
print(''.join(s))