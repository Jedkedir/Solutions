import sys
def solution():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    i = 1
    out = []
    for _ in range(t):
        n = data[i]
        i += 1
        end = i + n
        uniqe = set()
        while i < end:
            uniqe.add(data[i])
            i += 1
        b = sorted(uniqe)
        res = 0
        l = 0
        for r, val in enumerate(b):
            while val - b[l] >= n:
                l += 1
            window = r - l + 1
            if window > res:
                res = window
        out.append(str(res))
    sys.stdout.write("\n".join(out))
if __name__ == "__main__":
    solution()