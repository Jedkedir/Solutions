n, k = map(int, input().split())
a = sorted(map(int, input().split()))
candidate = a[max(0, min(n - 1, k - 1))]
res = -1
for j in [-1, 0, 1]:
    count = 0
    x = candidate + j
    if not (1 <= x <= 10**9):
        continue
    for i in a:
        if i <= x:
            count += 1
    if count == k:
        res = x
print(res)