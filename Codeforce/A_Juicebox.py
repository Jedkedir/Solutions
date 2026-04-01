import sys
def solution():
    _input = sys.stdin.read().split()
    if not _input:
        return
    it = iter(_input)
    t = int(next(it))
    res = []
    while t:
        n = int(next(it))
        k = int(next(it))
        brand_totals = {}
        for _ in range(k):
            b = int(next(it))
            c = int(next(it))
            if b in brand_totals:
                brand_totals[b] += c
            else:
                brand_totals[b] = c
        values = list(brand_totals.values())
        values.sort(reverse=True)
        earns = sum(values[:n])
        res.append(str(earns))
        t -= 1
    sys.stdout.write("\n".join(res) + "\n")
if __name__ == "__main__":
    solution()