n = int(input())
cards = list(map(int,input().split()))
l,r = 0,n-1
seraja = 0
dima = 0
seraja_turn = True
while l <= r:
    if cards[l] >= cards[r]:
        chosen = cards[l]
        l+=1
    else:
        chosen = cards[r]
        r-=1
    if seraja_turn:
        seraja += chosen
    else:
        dima += chosen
    seraja_turn = not seraja_turn
print(seraja,dima)