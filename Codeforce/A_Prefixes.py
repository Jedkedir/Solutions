n = int(input())
s = list(input().strip())

operations = 0

for i in range(0, n, 2):
    if s[i] == s[i+1]:
        # Change s[i] to opposite of s[i+1]? Actually both are same, so change one to opposite of itself.
        # But simpler: make first 'a', second 'b' or vice versa.
        if s[i] == 'a':
            s[i] = 'a'  # leave as is? Wait both are 'a' originally.
            # Make s[i]='a', s[i+1]='b'
            s[i+1] = 'b'
        else:  # both 'b'
            s[i] = 'b'
            s[i+1] = 'a'
        operations += 1

print(operations)
print(''.join(s))