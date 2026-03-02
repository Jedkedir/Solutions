cases = int(input())
while cases:
    s = input().strip()
    possible = False
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            possible = True
            break
    if possible:
        print(1)
    else:
        print(len(s))
    cases -= 1