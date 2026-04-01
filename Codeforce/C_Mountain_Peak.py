import sys
def solution():
    data = sys.stdin.read().split()
    it = iter(data)
    t = int(next(it))
    res = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        l = 0
        r = 2
        valid = False
        curr = []
        while r < n:
            if a[l]<a[l+1] and a[l+1]>a[r]:
                valid = True
                curr = [a[l], a[l+1], a[r]]
                break
            r+=1
            l+=1
        if valid:
            res.append("YES")
            res.append(" ".join(map(str, curr)))
        else:            
            res.append("NO")
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    solution()