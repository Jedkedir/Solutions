def solve():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    results = []
    for _ in range(q):
        n = int(next(it))
        s = next(it)
        t = next(it)
        if sorted(s) == sorted(t):
            results.append("YES")
        else:
            results.append("NO")
    print("\n".join(results))

if __name__ == "__main__":
    solve()

