import sys
def solution():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    for _ in range(t):
        n = int(next(it))
        s = next(it)
        mismatches = []
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                mismatches.append(i)
        if not mismatches:
            print("Yes")
        else:
            min_ = mismatches[0]
            max_ = mismatches[-1]
            valid = True
            for i in range(min_, max_ + 1):
                if s[i] == s[n - 1 - i]:
                    valid = False
                    break
            print("Yes" if valid else "No")
if __name__ == "__main__":
    solution()