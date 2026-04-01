import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    t = int(next(it))
    
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        a = [int(next(it)) for _ in range(n)]
       
        possible_starts = a[1 : n - k + 2]
        if any(x != 1 for x in possible_starts):
            print(1)
        else:
            print(2)

if __name__ == "__main__":
    solve()