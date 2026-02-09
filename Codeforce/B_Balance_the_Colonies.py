cases = int(input())
while cases:
    n = int(input())
    if n == 2:
        print('2')
    elif n == 3:
        print('3')
    else:
        print(n % 2)
    cases -= 1
