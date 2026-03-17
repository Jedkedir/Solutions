import sys


def solution():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n, s = int(next(it)), int(next(it))
    a = [int(next(it)) for _ in range(n)]
    l = 0
    curr = 0
    best = 0
    for right in range(n):
        curr += a[right]
        while curr > s:
            curr -= a[l]
            l += 1
        best = max(best, right - l + 1)
    print(best)
if __name__ == "__main__":
    solution()
