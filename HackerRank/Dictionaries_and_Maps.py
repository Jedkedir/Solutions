n = int(input())
phone_book = {}
for i in range(n):
    s = input().split()
    phone_book[s[0]] = s[1]
    
while True:
    try:
        name = input().strip()
        if not name:
            break
        if name in phone_book:
            print(f"{name}={phone_book[name]}")
        else:
            print("Not found")
    except EOFError:
        break

    
    