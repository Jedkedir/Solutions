Youssef_win, Youssef_time = map(int, input().split())
warriors = int(input())
while warriors:
    win, time = map(int, input().split())
    if  win > Youssef_win or (win == Youssef_win and time < Youssef_time):
        print("The Fallen Champion")
        break 
    warriors -= 1
if warriors == 0:
    print("The Champion Saves the Accused")