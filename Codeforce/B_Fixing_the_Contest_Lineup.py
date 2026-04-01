import sys
def solution():
    data = sys.stdin.read().split()
    it = iter(data)
    t = int(next(it))
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        b = [int(next(it)) for _ in range(n)]
        j = n - 1
        operations = 0
        for i in range(n-1, -1, -1):
            if a[i] > b[j]:
                operations += 1
            else:
                j -= 1
        print(operations)
if __name__ == "__main__":
    solution()