import sys
def merge_sorted_arrays(a, b, n, m):
    ptr1, ptr2 = 0, 0
    res = []
    while ptr1 < n and ptr2 < m:
        if a[ptr1] < b[ptr2]:
            res.append(a[ptr1])
            ptr1 += 1
        else:
            res.append(b[ptr2])
            ptr2 += 1
    res.extend(a[ptr1:])
    res.extend(b[ptr2:])
    return res

def solution():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n, m = int(next(it)), int(next(it))
    a = [int(next(it)) for _ in range(n)]
    b = [int(next(it)) for _ in range(m)]
    merged = merge_sorted_arrays(a, b, n, m)
    print(*merged)

if __name__ == "__main__":
    solution()