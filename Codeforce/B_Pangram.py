n = int(input())
s = input()
chars = set([ch.upper() for ch in s ])
if len(chars) == 26:
    print('YES')
else:
    print('NO')
