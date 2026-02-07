import sys
input = sys.stdin.read().split()
idx = 0
t = int(input[idx])
idx += 1
results = []
for _ in range(t):
    n = int(input[idx])
    k = int(input[idx + 1])
    idx += 2
    healths = list(map(int, input[idx : idx + n]))
    idx += n
    positions = list(map(int, input[idx : idx + n]))
    idx += n
    dist_health = {}
    for i in range(n):
        d = abs(positions[i])
        dist_health[d] = dist_health.get(d, 0) + healths[i]
    
    sorted_distances = sorted(dist_health.keys())
    
    possible = True
    bullets_spent = 0
    total_health_cleared = 0
    
    for d in sorted_distances:
        total_health_cleared += dist_health[d]
        if total_health_cleared > d * k:
            possible = False
            break
    
    results.append("YES" if possible else "NO")
print('\n'.join(results))
