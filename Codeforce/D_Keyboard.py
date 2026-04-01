import sys

def solution():
    data = sys.stdin.read().split()
    it = iter(data)
    t = int(next(it))
    res = []
    for _ in range(t):
        s = next(it)
        fine = set()
        i = 0
        while i < len(s):
            if i == len(s) - 1 or s[i] != s[i+1]:
                fine.add(s[i])
                i += 1
            else:
                i += 2
        res.append(''.join(sorted(fine)))
    sys.stdout.write("\n".join(res))
if __name__ == "__main__":
    solution()