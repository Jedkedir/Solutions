import sys
def solution():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        first = abs(a[0])
        smaller = 0
        for val in a[1:]:
            if abs(val) < first:
                smaller += 1
        if smaller <= n // 2:
            out.append("YES")
        else:
            out.append("NO")
    sys.stdout.write("\n".join(out))
if __name__ == "__main__":
    solution()