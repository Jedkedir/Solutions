from collections import Counter
days = int(input())
lookups = []
for _ in range(days):
    messages = int(input())
    for _ in range(messages):
        name, hour = input().split()
        lookups.append((name, hour))
counts = Counter(lookups)
found = False
percent = 0.8 * days
for pair in counts:
    if counts[pair] >= percent:
        found = True
        break
if found:
    print('YES')
else:
    print('NO')