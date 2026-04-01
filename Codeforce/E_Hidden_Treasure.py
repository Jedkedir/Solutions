import sys
def solution():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n, m = int(next(it)), int(next(it))
    min_ = 1
    max_ = n
    for _ in range(1, m + 1):
        next(it)  
        next(it)  
        direction = next(it)  
        next(it)
        if direction == "left":
            num = int(next(it))
            max_ = min(max_, num - 1)
        elif direction == "right":
            num = int(next(it))
            min_ = max(min_, num + 1)
    if min_ > max_:
        print(-1)
    else:
        print(max_ - min_ + 1)
if __name__ == "__main__":
    solution()