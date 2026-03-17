import sys
def strictly_less_than(arr1, arr2, n):
    res = []
    ptr = 0
    for num in arr2:
        while ptr < n and arr1[ptr] < num:
            ptr += 1
        res.append(ptr)
    return res
def solution():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n,m = int(next(it)), int(next(it))
    a = [int(next(it)) for _ in range(n)]
    b = [int(next(it)) for _ in range(m)]
    ans = strictly_less_than(a, b, n)
    print(*ans)
if __name__ == "__main__":
    solution()