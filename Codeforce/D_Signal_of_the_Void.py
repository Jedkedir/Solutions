t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    hubs = []
    for i in range(n):
        if b[i] < p:
            hubs.append((b[i], a[i]))
    hubs.sort()
    total_cost = p  
    Remaining = n - 1
    for cost, cap in hubs:
        if Remaining <= 0:
            break
        take = min(Remaining, cap)
        total_cost += take * cost
        Remaining -= take
    total_cost += Remaining * p
    print(total_cost)