import sys
def solution():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    pattern = "meow"
    for _ in range(t):
        n = int(next(it))
        s = next(it).lower()
        uniqe = []
        for ch in s:
            if not uniqe or uniqe[-1] != ch:
                uniqe.append(ch)
        if len(uniqe) != 4 or "".join(uniqe) != pattern:
            print("NO")
        else:
            print("YES")
if __name__ == "__main__":
    solution()

        