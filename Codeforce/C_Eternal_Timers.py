t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    min_val = min(arr)
    max_val = max(arr)
    if max_val <= 2 * min_val:
        print("YES")
    else:
        print("NO")