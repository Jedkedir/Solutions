password = input()
n = int(input())
words = []
while n:
    words.append(input())
    n -= 1
if password in words:
    print('YES')
else:
    first,second = False,False
    for word in words:
        if word[1] == password[0]:
            first = True
        if word[0]==password[1]:
            second= True
    if first and second:
        print('YES')
    else:
        print('NO')