from collections import Counter
def isSubset(a, b):
    a_counts = Counter(a)
    b_counts = Counter(b)
    for value, count in b_counts.items():
        if a_counts[value] < count:
            return False
    return True

