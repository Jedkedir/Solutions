amount = int(input())
for _ in range(amount):
    words = input()
    for word in words.split():
        print(word[0],end="")
    print()