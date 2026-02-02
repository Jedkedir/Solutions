amount = int(input())
while amount:
    word = input()
    n = len(word)
    if n > 10:
        print(word[0]+str(n-2)+word[-1])
    else:
        print(word)
    amount -= 1