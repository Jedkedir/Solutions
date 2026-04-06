import sys
def solution():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    best = 0
    curr = 0
    for val in a + a:
        if val == 1:
            curr += 1
            if curr > best:
                best = curr
        else:
            curr = 0
    if best > n:
        best = n
    print(best)
if __name__ == "__main__":
    solution()